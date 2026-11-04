#!/usr/bin/env python3
"""
Create tornado plots for all result parameters in a sensitivity export file.

This version includes the MBYAanalysis.txt parsing logic:
- supports FIELD and Well result columns in the same file;
- handles a leading blank first header cell in TXT/TSV exports;
- recognises Low/High cells written as percentages, e.g. '+0.156%; -0.103%';
- treats '+0; +0' as a zero sensitivity row, not as an error;
- skips columns that contain only zero/base-value sensitivities;
- removes trailing summary rows such as 'Max. deviation';
- creates high-resolution PNG plots and a sharp vector multipage PDF.

Usage:
    python create_all_parameter_tornado_plots_vector_pdf_MBYA.py "C:\\path\\MBYAanalysis.txt"

If no path is provided, the script prompts for it.
Supported input formats: TXT, TSV, DAT, CSV, XLSX, XLSM, XLS.
"""

from __future__ import annotations
import argparse
import math
import re
import sys
import zipfile
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

# -----------------------------------------------------------------------------
# Final approved plot style
# -----------------------------------------------------------------------------
LOW_COLOUR = "#4472C4"          # blue
HIGH_COLOUR = "#70AD47"         # green
LOW_LABEL_COLOUR = "#1F4E79"
HIGH_LABEL_COLOUR = "#548235"
LABEL_FONT_SIZE = 8.8            # 10 percent larger than 8 pt
TITLE_FONT_SIZE = 11
TOP_N = 15
PNG_DPI = 230
FIGURE_SIZE = (15.6, 8.2)
TITLE_Y = 0.965                  # title shifted down into reserved band
TOP_EMPTY_ROWS = 2.25            # prevents lowered title from covering data
BOTTOM_EMPTY_ROWS = 0.75

NUMBER_PATTERN = re.compile(
    r"([+-]?\d+(?:\.\d+)?(?:e[+-]?\d+)?)\s*%?",
    flags=re.IGNORECASE,
)


def normalise(value: object) -> str:
    """Normalise text from headers and parameter names."""
    if value is None:
        return ""

    return str(value).strip().replace("\\_", "_")


def make_unique_headers(headers: list[str]) -> list[str]:
    """Return unique, non-empty headers without silently dropping columns."""
    output: list[str] = []
    seen: dict[str, int] = {}
    for index, raw_header in enumerate(headers):
        header = normalise(raw_header)
        if not header or header.lower() in {"nan", "none"}:
            header = "Sensitivity parameter" if index == 0 else f"Result_{index}"

        seen[header] = seen.get(header, 0) + 1
        if seen[header] == 1:
            output.append(header)
        else:
            output.append(f"{header} [{seen[header]}]")

    return output


def load_txt_like_file(path: Path) -> pd.DataFrame:
    """Load tab-delimited TXT/TSV/DAT files, preserving a blank first header."""
    raw_lines = [
        line.rstrip("\r\n")
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines()
        if line.strip()
    ]

    if not raw_lines:
        raise ValueError("The input file is empty.")

    raw_rows = [[normalise(cell) for cell in line.split("\t")] for line in raw_lines]
    headers = make_unique_headers(raw_rows[0])
    width = len(headers) 
    rows = []
    for row in raw_rows[1:]:
        rows.append(row[:width] + [""] * max(0, width - len(row)))

    return pd.DataFrame(rows, columns=headers)
 

def load_data(path: Path) -> pd.DataFrame:
    """Load supported input formats into a clean dataframe."""
    suffix = path.suffix.lower()
    if suffix in {".txt", ".tsv", ".dat"}:
        dataframe = load_txt_like_file(path)
    elif suffix == ".csv":
        dataframe = pd.read_csv(path, sep=None, engine="python", dtype=str)
        dataframe.columns = make_unique_headers(list(dataframe.columns))
    elif suffix in {".xlsx", ".xlsm"}:
        dataframe = pd.read_excel(path, engine="openpyxl", dtype=str)
        dataframe.columns = make_unique_headers(list(dataframe.columns))
    elif suffix == ".xls":
        dataframe = pd.read_excel(path, engine="xlrd", dtype=str)
        dataframe.columns = make_unique_headers(list(dataframe.columns))
    else:
        raise ValueError("Unsupported input type. Use TXT, TSV, DAT, CSV, XLSX, XLSM or XLS.")
 
    dataframe = dataframe.dropna(axis=0, how="all").dropna(axis=1, how="all")
    dataframe = dataframe.loc[:, [c for c in dataframe.columns if not c.lower().startswith("unnamed:")]]
    if dataframe.empty or len(dataframe.columns) < 2:
        raise ValueError("The input must contain one sensitivity column and at least one result column.")

    first_column = dataframe.columns[0]
    dataframe = dataframe.rename(columns={first_column: "Sensitivity parameter"})
    dataframe["Sensitivity parameter"] = dataframe["Sensitivity parameter"].map(normalise)

    # Remove summary/footer rows before identifying result columns.
    lower_names = dataframe["Sensitivity parameter"].str.lower()
    dataframe = dataframe[
        ~lower_names.str.startswith(("max. deviation", "max deviation", "maximum deviation"), na=False)
    ].copy()

    return dataframe


def extract_number_pair(cell: object) -> tuple[float, float]:
    """
    Extract the first two numeric values from a Low/High cell.
    Handles both percentage cells such as '+0.156%; -0.103%' and MBYA zero
    cells such as '+0; +0'. Values are returned as percentages or percentage
    changes as provided by the source file.
    """
    text = str(cell)
    values = [float(match) for match in NUMBER_PATTERN.findall(text)]
    if len(values) < 2:
        values += [math.nan] * (2 - len(values))

    return values[0], values[1]


def is_valid_pair_cell(cell: object) -> bool:
    values = extract_number_pair(cell)
    return not (math.isnan(values[0]) or math.isnan(values[1]))


def is_non_zero_pair(cell: object) -> bool:
    low, high = extract_number_pair(cell)
    if math.isnan(low) or math.isnan(high):
        return False

    return abs(low) > 0 or abs(high) > 0


def identify_result_columns(dataframe: pd.DataFrame) -> tuple[list[str], list[str]]:
    """
    Identify result columns for MBYA-style exports.
    A column is included only if it has at least one valid Low/High pair and at
    least one non-zero Low/High pair. Columns containing only '+0; +0' or blank
    values are skipped automatically.
    """
    included: list[str] = []
    skipped: list[str] = []
    for column in dataframe.columns[1:]:
        series = dataframe[column].fillna("")
        valid_pairs = int(series.map(is_valid_pair_cell).sum())
        non_zero_pairs = int(series.map(is_non_zero_pair).sum())
        if valid_pairs > 0 and non_zero_pairs > 0:
            included.append(column)
        else:
            skipped.append(column)

    return included, skipped


def format_percentage(value: float) -> str:
    absolute = abs(value)
    if absolute >= 10:
        return f"{value:.1f}%"

    if absolute >= 1:
        return f"{value:.2f}%"

    if absolute >= 0.01:
        return f"{value:.3f}%"

    return f"{value:.2e}%"


def safe_filename(value: str, maximum_length: int = 150) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("_")
    return (cleaned or "Result")[:maximum_length]


def friendly_title(column: str) -> str:
    """Make a readable plot title while preserving the source meaning."""
    well_match = re.match(r"^Well\s+'([^']+)'\s+(.+)$", column, flags=re.IGNORECASE)
    if well_match:
        return f"{well_match.group(1)} - {well_match.group(2)}"

    objective_match = re.match(
        r"^Objective Function\s+'([^']+)'\s*(.*)$",
        column,
        flags=re.IGNORECASE,
    )

    if objective_match:
        suffix = objective_match.group(2).strip()
        return f"Objective Function {objective_match.group(1)}" + (f" - {suffix}" if suffix else "")

    return column


def create_plot(
    dataframe: pd.DataFrame,
    result_column: str,
    output_png: Path,
    pdf: PdfPages,
    top_n: int,
) -> dict[str, object] | None:

    parsed = dataframe[result_column].map(extract_number_pair)
    data = pd.DataFrame(
        {
            "Sensitivity parameter": dataframe["Sensitivity parameter"],
            "Low": parsed.map(lambda pair: pair[0]),
            "High": parsed.map(lambda pair: pair[1]),
        }
    )
 
    data = data.dropna(subset=["Low", "High"], how="all")
    data["Impact"] = data[["Low", "High"]].abs().max(axis=1)
    data = data[data["Impact"] > 0].sort_values("Impact", ascending=False).head(top_n)
    plot_data = data.sort_values("Impact").reset_index(drop=True)
    if plot_data.empty:
        return None

    scale = max(1.0, float(plot_data[["Low", "High"]].abs().max().max()))
    label_padding = 0.08 * scale
    label_separation = 0.22 * scale
    x_min = min(float(plot_data["Low"].min()), float(plot_data["High"].min()), 0.0) - 0.65 * scale
    x_max = max(float(plot_data["Low"].max()), float(plot_data["High"].max()), 0.0) + 0.85 * scale
    figure, axis = plt.subplots(figsize=FIGURE_SIZE)
    y_positions = list(range(len(plot_data)))
    axis.barh(y_positions, plot_data["Low"], color=LOW_COLOUR, label="Low side", height=0.72)
    axis.barh(y_positions, plot_data["High"], color=HIGH_COLOUR, label="High side", height=0.45)
    for row_index, (low_value, high_value) in enumerate(zip(plot_data["Low"], plot_data["High"])):
        labels: list[dict[str, object]] = []
        if not math.isnan(low_value):
            labels.append({"side": "Low", "value": low_value, "colour": LOW_LABEL_COLOUR})

        if not math.isnan(high_value):
            labels.append({"side": "High", "value": high_value, "colour": HIGH_LABEL_COLOUR})

        same_side = len(labels) == 2 and ((labels[0]["value"] >= 0) == (labels[1]["value"] >= 0))
        if same_side:
            sign = 1 if labels[0]["value"] >= 0 else -1
            outermost = max(labels[0]["value"], labels[1]["value"]) if sign > 0 else min(labels[0]["value"], labels[1]["value"])
            ordered = sorted(labels, key=lambda item: 0 if item["side"] == "High" else 1)
            x_positions = [outermost + sign * label_padding, outermost + sign * (label_padding + label_separation)]
            horizontal_alignment = "left" if sign > 0 else "right"
        else:
            ordered = labels
            x_positions = [
                item["value"] + (1 if item["value"] >= 0 else -1) * label_padding
                for item in ordered
            ]

            horizontal_alignment = None

        for item, x_position in zip(ordered, x_positions):
            alignment = horizontal_alignment or ("left" if item["value"] >= 0 else "right")
            axis.text(
                x_position,
                row_index,
                format_percentage(item["value"]),
                va="center",
                ha=alignment,
                fontsize=LABEL_FONT_SIZE,
                color=item["colour"],
                clip_on=False,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.85, "pad": 0.5},
            )

            x_min = min(x_min, x_position - 0.18 * scale)
            x_max = max(x_max, x_position + 0.18 * scale)

    axis.set_xlim(x_min, x_max)
    axis.set_ylim(-BOTTOM_EMPTY_ROWS, len(plot_data) - 1 + TOP_EMPTY_ROWS)
    axis.set_yticks(y_positions)
    axis.set_yticklabels(plot_data["Sensitivity parameter"])
    axis.axvline(0, color="black", linewidth=0.8)
    axis.text(
        0.5,
        TITLE_Y,
        friendly_title(result_column),
        transform=axis.transAxes,
        ha="center",
        va="top",
        fontsize=TITLE_FONT_SIZE,
        color="black",
        bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.85, "pad": 1.0},
    )

    axis.set_xlabel("Change vs Base (%)")
    axis.legend(loc="lower left", frameon=True)
    axis.grid(axis="x", alpha=0.3)
    figure.tight_layout(pad=0.9)
 
    # PNG remains high-resolution; PDF is sharp because the original Matplotlib
    # figure is saved directly as a vector page rather than as an embedded PNG.
    figure.savefig(output_png, dpi=PNG_DPI, bbox_inches="tight")
    pdf.savefig(figure, bbox_inches="tight")
    plt.close(figure)
    strongest = data.iloc[0]
    return {
        "Result parameter": result_column,
        "Plot title": friendly_title(result_column),
        "Top sensitivity parameter": strongest["Sensitivity parameter"],
        "Maximum absolute impact (%)": strongest["Impact"],
        "Plotted sensitivities": len(plot_data),
        "PNG file": output_png.name,
    }


def build_outputs(input_path: Path, top_n: int = TOP_N) -> tuple[Path, Path, Path, Path, Path]:
    dataframe = load_data(input_path)
    result_columns, skipped_columns = identify_result_columns(dataframe)
    if not result_columns:
        raise ValueError("No result columns containing non-zero Low/High pairs were found.")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_directory = input_path.parent / f"All_Parameter_Tornado_Plots_{timestamp}"
    png_directory = output_directory / "PNG"
    png_directory.mkdir(parents=True, exist_ok=False)
    pdf_path = output_directory / "All_Parameter_Tornado_Plots_Vector.pdf"
    summary_rows: list[dict[str, object]] = []
    used_names: dict[str, int] = {}
    with PdfPages(pdf_path) as pdf:
        for sequence, result_column in enumerate(result_columns, start=1):
            base_name = safe_filename(result_column)
            used_names[base_name] = used_names.get(base_name, 0) + 1
            suffix = "" if used_names[base_name] == 1 else f"_{used_names[base_name]}"
            png_path = png_directory / f"{sequence:03d}_{base_name}{suffix}.png"
            summary = create_plot(dataframe, result_column, png_path, pdf, top_n)
            if summary is not None:
                summary_rows.append(summary)

    if not summary_rows:
        raise ValueError("All identified result columns contained only zero or blank sensitivities.")

    summary_path = output_directory / "All_Parameter_Tornado_Plots_Summary.csv"
    pd.DataFrame(summary_rows).to_csv(summary_path, index=False)
    skipped_path = output_directory / "Skipped_Columns.txt"
    skipped_path.write_text(
        "Columns skipped because no non-zero Low/High pairs were detected:\n"
        + ("\n".join(skipped_columns) if skipped_columns else "None"),
        encoding="utf-8",
    )

    zip_path = output_directory / "All_Parameter_Tornado_Plots.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.write(pdf_path, arcname=pdf_path.name)
        archive.write(summary_path, arcname=summary_path.name)
        archive.write(skipped_path, arcname=skipped_path.name)
        for png_path in sorted(png_directory.glob("*.png")):
            archive.write(png_path, arcname=f"PNG/{png_path.name}")

    return output_directory, pdf_path, zip_path, summary_path, skipped_path
 

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create vector-PDF tornado plots for every result parameter in a sensitivity file."
    )

    parser.add_argument(
        "input_file",
        nargs="?",
        help="Full path to the TXT/TSV/DAT/CSV/XLSX/XLSM/XLS input file.",
    )

    parser.add_argument(
        "--top-n",
        type=int,
        default=TOP_N,
        help=f"Number of sensitivities to plot per result parameter. Default: {TOP_N}.",
    )

    arguments = parser.parse_args()
    raw_path = arguments.input_file or input("Enter the full path to the input data file: ").strip().strip('"')
    input_path = Path(raw_path).expanduser()
    if not input_path.is_file():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    output, pdf, archive, summary, skipped = build_outputs(input_path.resolve(), top_n=arguments.top_n)
    print("Completed successfully.")
    print(f"Output folder:  {output}")
    print(f"Vector PDF:     {pdf}")
    print(f"ZIP package:    {archive}")
    print(f"Summary CSV:    {summary}")
    print(f"Skipped report: {skipped}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)