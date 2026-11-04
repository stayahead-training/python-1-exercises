# importing libraries
import math
from dataclasses import dataclass
from typing import List

# for m to ft conversion, removed as now data should be entered in ft
FT_PER_M = 1


def _emit(msg: str):
    try:
        log(msg)  # type: ignore[name-defined]
    except Exception:
        print(msg)


# ============================================================
# USER SETTING: how many SATNUM regions (tables) to create?
# ============================================================
N_REGIONS = 3  # <-- set to what is relevant to your project

# ============================================================
# 2) READ INPUTS for region i
# ============================================================
def sv(x: List[str], i: int) -> float:
    return float(str(x[i]).strip())


@dataclass(frozen=True)
class Inputs:
    hentImin: float; hentImax: float; swImax: float; poroImin: float; swImin: float; poroImax: float
    hentIexp: float; nI: float; mI: float; poro_value: float; hswc: float; rho_o: float; rho_w: float
    KROCW: float; EXP_OW: float; SORG: float; KRGCL: float; EXP_OG: float; sowcr: float
    KRWIRO: float; EXP_W: float; sgcr: float; KROGCG: float; EXP_G: float


def build_inputs_for_region(i: int) -> Inputs:
    return Inputs(
        hentImin=sv(hentImin, i),
        hentImax=sv(hentImax, i),
        swImax=sv(swImax, i),
        poroImin=sv(poroImin, i),
        swImin=sv(swImin, i),
        poroImax=sv(poroImax, i),
        hentIexp=sv(hentIexp, i),
        nI=sv(nI, i),
        mI=sv(mI, i),
        poro_value=sv(poro_value, i),
        hswc=sv(hswc, i),
        rho_o=sv(rho_o, i),
        rho_w=sv(rho_w, i),
        KROCW=sv(KROCW, i),
        EXP_OW=sv(EXP_OW, i),
        SORG=sv(SORG, i),
        KRGCL=sv(KRGCL, i),
        EXP_OG=sv(EXP_OG, i),
        sowcr=sv(sowcr, i),
        KRWIRO=sv(KRWIRO, i),
        EXP_W=sv(EXP_W, i),
        sgcr=sv(sgcr, i),
        KROGCG=sv(KROGCG, i),
        EXP_G=sv(EXP_G, i),
    )


# ============================================================
# 3) CALCULATION to replicate EXCEL spreadsheet
# ============================================================
def excel_iferror(fn, fallback=0.0):
    try:
        v = float(fn())
        if math.isnan(v) or math.isinf(v):
            return fallback
        return v
    except Exception:
        return fallback


def safe_pow(base, exp):
    if base < 0 and abs(exp - round(exp)) > 1e-12:
        raise ValueError("invalid power")
    
    return base ** exp


def round_list(vals, ndp):
    return [round(float(v), ndp) for v in vals]


def compute_params_tables(inp: Inputs, region_idx: int = None):
    # overwrite poro_value using midpoint formula
    poro_value = 0.5 * (inp.poroImin + inp.poroImax)
    prefix = f"[Region {region_idx+1}]" if region_idx is not None else "[Region]"
    _emit(f"{prefix} poro_value used (midpoint) = {poro_value:.4f}  "
          f"(poroImin={inp.poroImin:.4f}, poroImax={inp.poroImax:.4f})")

    hmin_ft = inp.hentImin * FT_PER_M
    hmax_ft = inp.hentImax * FT_PER_M
    hSwc_ft = inp.hswc * FT_PER_M

    lmbda = inp.nI * poro_value + inp.mI

    a = (inp.swImin - inp.swImax) / (inp.poroImax - inp.poroImin)
    b = inp.swImin - ((inp.swImin - inp.swImax) / (inp.poroImax - inp.poroImin)) * inp.poroImax
    SWCON = a * poro_value + b 

    X = ((inp.poroImax - poro_value) / (inp.poroImax - inp.poroImin)) * math.exp(
        inp.hentIexp * ((inp.poroImin - poro_value) / (inp.poroImax - inp.poroImin))
    )

    # ---- SWOF ----
    step_sw = (1.0 - inp.sowcr - SWCON) / 19.0
    Sw = [SWCON + i * step_sw for i in range(20)] + [1.0]

    def krw(sw):
        return inp.KRWIRO * safe_pow((sw - SWCON) / (1.0 - SWCON - inp.sowcr), inp.EXP_W)

    def kro(sw):
        return excel_iferror(
            lambda: inp.KROCW
            * safe_pow((1.0 - inp.sowcr - sw) / (1.0 - inp.sowcr - SWCON), inp.EXP_OW),
            fallback=0.0,
        )

    A = hmin_ft + (hmax_ft - hmin_ft) * X
    A_pow = safe_pow(A, -lmbda)
    hSwc_pow = safe_pow(hSwc_ft, -lmbda)
    denom = 1.0 - SWCON

    def height_ft(sw, first):
        if first:
            return hSwc_ft
        return excel_iferror(
            lambda: safe_pow(
                (A_pow - ((1.0 - sw) / denom) * (A_pow - hSwc_pow)),
                (-1.0 / lmbda),
            ),
            fallback=0.0,
        )

    def pc1(h):
        return (h * (inp.rho_w - inp.rho_o)) / 144.0

    krw_list, kro_list, pcow_list = [], [], []
    for i, sw in enumerate(Sw):
        h = height_ft(sw, i == 0)
        krw_list.append(excel_iferror(lambda sw=sw: krw(sw), 0.0))
        kro_list.append(kro(sw))
        pcow_list.append(pc1(h))

    # endpoint behavior to make sure last table row is maintained
    krw_list[0] = 0.0
    Sw[-1] = 1.0
    krw_list[-1] = 1.0
    kro_list[-1] = 0.0

    # ---- SGOF ----
    step_sg = (1.0 - SWCON - inp.SORG - inp.sgcr) / 18.0
    Sg = [0.0, inp.sgcr]
    while len(Sg) < 20:
        Sg.append(Sg[-1] + step_sg)

    def Krg(sg):
        return inp.KRGCL * safe_pow(
            (sg - inp.sgcr) / (1.0 - SWCON - inp.SORG - inp.sgcr),
            inp.EXP_G,
        )

    def Krog(sg):
        return excel_iferror(
            lambda: inp.KROGCG * safe_pow((1.0 - sg / (1.0 - SWCON - inp.SORG)), inp.EXP_OG),
            fallback=0.0,
        )

    krg_list, krog_list = [], []
    for i, sg in enumerate(Sg):
        krg_list.append(0.0 if i == 0 else excel_iferror(lambda sg=sg: Krg(sg), 0.0))
        krog_list.append(Krog(sg))

    pcg_list = [0.0] * len(Sg)

    return [
        round_list(Sw, 6),
        round_list(krw_list, 7),
        round_list(kro_list, 4),
        round_list(pcow_list, 6),
        round_list(Sg, 6),
        round_list(krg_list, 6),
        round_list(krog_list, 4),
        pcg_list,
    ]


# ============================================================
# 4) LOOP REGIONS -> CREATE TABLES
# ============================================================
_all_vectors = {
    "hentImin": hentImin,
    "hentImax": hentImax,
    "swImax": swImax,
    "poroImin": poroImin,
    "swImin": swImin,
    "poroImax": poroImax,
    "hentIexp": hentIexp,
    "nI": nI,
    "mI": mI,
    "poro_value": poro_value,
    "hswc": hswc,
    "rho_o": rho_o,
    "rho_w": rho_w,
    "KROCW": KROCW,
    "EXP_OW": EXP_OW,
    "SORG": SORG,
    "KRGCL": KRGCL,
    "EXP_OG": EXP_OG,
    "sowcr": sowcr,
    "KRWIRO": KRWIRO,
    "EXP_W": EXP_W,
    "sgcr": sgcr,
    "KROGCG": KROGCG,
    "EXP_G": EXP_G,
}
for _name, _vec in _all_vectors.items():
    if len(_vec) < N_REGIONS:
        raise ValueError(f"Variable '{_name}' has {len(_vec)} entries, but N_REGIONS={N_REGIONS}.")

# ------------------------------------------------------------
# EXPORT SETUP: use the same timestamped folder as the main workflow
# ------------------------------------------------------------
BASE_DIR = "T:/ProjectData/tNav/Tests/Shoebox/"
import os
_run_marker_file = BASE_DIR + "latest_tnavigator_run_folder.txt"
OUTPUT_DIR = ""
if os.path.exists(_run_marker_file):
    _mf = open(_run_marker_file, "r")
    OUTPUT_DIR = _mf.read().strip()
    _mf.close()
if OUTPUT_DIR == "":
    try:
        RUN_TIMESTAMP
    except:
        from datetime import datetime
        RUN_TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
    OUTPUT_DIR = BASE_DIR + "run_" + RUN_TIMESTAMP + "/"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

_emit(f"Creating {N_REGIONS} RP tables (one per region index 0..{N_REGIONS-1})...")

for region_idx in range(N_REGIONS):
    inp_i = build_inputs_for_region(region_idx)

    # ------------------------------------------------------------
    # EXPORT: one RP input-variable snapshot per SATNUM region
    # ------------------------------------------------------------
    ZONE_VALUE_RP = zoneIvalue[region_idx]
    ZONE_NAME_RP = zoneIname[region_idx]
    _safe_zone_name = str(ZONE_NAME_RP).replace(" ", "_").replace("/", "_")
    _export_file = OUTPUT_DIR + "workflow_relperm_input_variables_SATNUM_%s_%s.txt" % (str(ZONE_VALUE_RP), _safe_zone_name)
    _f = open(_export_file, "w")
    print("tNavigator workflow relperm input-variable snapshot", file=_f)
    print("Output folder: %s" % OUTPUT_DIR, file=_f)
    print("SATNUM / region index: %s" % str(region_idx), file=_f)
    print("ZONE_VALUE: %s" % str(ZONE_VALUE_RP), file=_f)
    print("ZONE_NAME: %s" % str(ZONE_NAME_RP), file=_f)
    print("", file=_f)
    print("=== CURRENT REGION INPUTS ===", file=_f)
    print("hentImin=%s" % str(inp_i.hentImin), file=_f)
    print("hentImax=%s" % str(inp_i.hentImax), file=_f)
    print("swImax=%s" % str(inp_i.swImax), file=_f)
    print("poroImin=%s" % str(inp_i.poroImin), file=_f)
    print("swImin=%s" % str(inp_i.swImin), file=_f)
    print("poroImax=%s" % str(inp_i.poroImax), file=_f)
    print("hentIexp=%s" % str(inp_i.hentIexp), file=_f)
    print("nI=%s" % str(inp_i.nI), file=_f)
    print("mI=%s" % str(inp_i.mI), file=_f)
    print("poro_value=%s" % str(inp_i.poro_value), file=_f)
    print("hswc=%s" % str(inp_i.hswc), file=_f)
    print("rho_o=%s" % str(inp_i.rho_o), file=_f)
    print("rho_w=%s" % str(inp_i.rho_w), file=_f)
    print("KROCW=%s" % str(inp_i.KROCW), file=_f)
    print("EXP_OW=%s" % str(inp_i.EXP_OW), file=_f)
    print("SORG=%s" % str(inp_i.SORG), file=_f)
    print("KRGCL=%s" % str(inp_i.KRGCL), file=_f)
    print("EXP_OG=%s" % str(inp_i.EXP_OG), file=_f)
    print("sowcr=%s" % str(inp_i.sowcr), file=_f)
    print("KRWIRO=%s" % str(inp_i.KRWIRO), file=_f)
    print("EXP_W=%s" % str(inp_i.EXP_W), file=_f)
    print("sgcr=%s" % str(inp_i.sgcr), file=_f)
    print("KROGCG=%s" % str(inp_i.KROGCG), file=_f)
    print("EXP_G=%s" % str(inp_i.EXP_G), file=_f)
    _f.close()
    try:
        log("Exported %s" % _export_file)
    except:
        print("Exported %s" % _export_file)
    params_tables = compute_params_tables(inp_i, region_idx)

    variant_name = f"RP_Table_{region_idx+1}"

    adjust_rp_table(
        variant_name=variant_name,
        mode="create",
        phases="oil_and_gas",
        type="swof_sgof",
        preset="intermediate_wet",
        use_cap_pressure_from_table=False,
        use_baker_for_water_from_table=False,
        use_baker_for_gas_from_table=False,
        use_add_miscible_from_table=False,
        use_liquid_saturations_from_table=False,
        jfunc_flags=[0, 0, 0, 0, 0, 0],
        params_tables=params_tables,
    )

    _emit(f"Done: created/updated RP table '{variant_name}' using inputs row {region_idx}")

_emit("All regions processed.")