from pathlib import Path


def find_files(folder: str, pattern: str = "*") -> list[Path]:
    """Find all files in a folder."""

    path = Path(folder)

    
    files_list = []

    for file in path.rglob(pattern):
        if file.is_file():
            files_list.append(file)

    return files_list

