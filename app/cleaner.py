import re
from pathlib import Path

def clean_filename(filename: str) -> str:
    """
    Clean a filename by removing special characters and replacing spaces with underscores and preserve
    the extension of the filename."""

    path = Path(filename)

    stem = path.stem
    extension = path.suffix

    stem = stem.strip()
    stem = re.sub(r"[^a-zA-Z0-9]+", "_", stem) # remove special characters and spaces with underscores.
    stem = stem.strip("_")
    

    return stem + extension


