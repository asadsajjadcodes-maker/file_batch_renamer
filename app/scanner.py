from pathlib import Path


def find_files(folder: str, pattern: str = "*") -> list[Path]:
    """Find all files in a folder."""

    path = Path(folder)

    if not path.exists():
        err = f"Folder '{folder}' does not exist."
        return err
    else:
        files_list = []
        for file in path.rglob(pattern):
            if file.is_file():
                files_list.append(file)

    return files_list

# for test purpose only 
test_path = Path(".")
for files in find_files(test_path, "*.py"):
    print(files)
    