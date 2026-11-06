import os
import shutil
from pathlib import Path


def select_files(files):
    while True:
        choice = input(
            "\nEnter file numbers separated by commas, 'all', or 'q' to quit: "
        ).strip().lower()

        if choice == "q":
            return []
        if choice == "all":
            return files

        try:
            numbers = [int(value.strip()) for value in choice.split(",")]
            if not numbers or any(number < 1 or number > len(files) for number in numbers):
                raise ValueError

            # Preserve the order entered while removing duplicates.
            return [files[number - 1] for number in dict.fromkeys(numbers)]
        except ValueError:
            print("Invalid selection. Enter numbers from the displayed list.")


def report_search_error(error):
    print(f"Could not search {error.filename}: {error.strerror}")


def main():
    root_input = input("Directory to search [current directory]: ").strip()
    root = Path(root_input).expanduser() if root_input else Path.cwd()

    if not root.is_dir():
        print(f"Not a directory: {root}")
        return

    search_text = input("Filename to search for (partial matches allowed): ").strip()
    if not search_text:
        print("Please enter a filename or part of a filename.")
        return

    matches = []
    for directory, _, filenames in os.walk(root, onerror=report_search_error):
        for filename in filenames:
            path = Path(directory) / filename
            if (
                search_text.casefold() in filename.casefold()
                and not path.is_symlink()
                and path.is_file()
            ):
                matches.append(path)

    matches.sort(key=lambda path: str(path).casefold())

    if not matches:
        print("No matching files found.")
        return

    print("\nSearch results:")
    for number, path in enumerate(matches, start=1):
        print(f"{number}. {path}")

    selected = select_files(matches)
    if not selected:
        print("No files selected.")
        return

    while True:
        action = input("Copy or move? [c/m]: ").strip().lower()
        if action in ("c", "m"):
            break
        print("Enter 'c' to copy or 'm' to move.")

    destination_input = input("Destination directory: ").strip()
    if not destination_input:
        print("A destination directory is required.")
        return

    destination = Path(destination_input).expanduser()
    try:
        destination.mkdir(parents=True, exist_ok=True)
    except OSError as error:
        print(f"Could not create or access destination: {error}")
        return

    for source in selected:
        target = destination / source.name
        if os.path.lexists(target):
            print(f"Skipped {source}: destination already exists: {target}")
            continue

        try:
            if action == "c":
                shutil.copy2(source, target)
                print(f"Copied: {source} -> {target}")
            else:
                shutil.move(str(source), str(target))
                print(f"Moved: {source} -> {target}")
        except OSError as error:
            print(f"Could not process {source}: {error}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCancelled.")