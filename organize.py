import shutil
import sys
from pathlib import Path

# ---------- Settings ----------
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv", ".pptx"],
    "Archives": [".zip", ".rar", ".7z"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Video": [".mp4", ".mkv", ".avi"],
}
OTHER_FOLDER = "Other"
# ------------------------------


def get_category(file):
    """Return the category name for a file based on its extension."""
    extension = file.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return OTHER_FOLDER


def unique_destination(destination):
    """If a file with the same name exists, add a number: name_1.ext, name_2.ext"""
    if not destination.exists():
        return destination
    counter = 1
    while True:
        candidate = destination.with_name(f"{destination.stem}_{counter}{destination.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def organize(folder, dry_run):
    files = [f for f in folder.iterdir() if f.is_file()]
    if not files:
        print("No files to organize.")
        return

    moved = 0
    for file in files:
        category = get_category(file)
        target_folder = folder / category
        destination = unique_destination(target_folder / file.name)

        if dry_run:
            print(f"[preview] {file.name} -> {category}/{destination.name}")
        else:
            target_folder.mkdir(exist_ok=True)
            shutil.move(str(file), str(destination))
            print(f"Moved: {file.name} -> {category}/{destination.name}")
        moved += 1

    action = "would be moved" if dry_run else "moved"
    print(f"Done: {moved} file(s) {action}.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python organize.py <folder> [--run]")
        print("Without --run, it only shows a preview and changes nothing.")
        sys.exit(1)

    folder = Path(sys.argv[1])
    if not folder.exists() or not folder.is_dir():
        print(f"Error: '{folder}' is not a valid folder.")
        sys.exit(1)

    dry_run = "--run" not in sys.argv
    organize(folder, dry_run)


if __name__ == "__main__":
    main()