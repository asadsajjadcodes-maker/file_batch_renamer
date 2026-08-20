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
    stem = stem.lower()

    return stem + extension


# test the function with some filenames .
print(clean_filename("example file.txt"))
print(clean_filename("   My!!! Vacation@@@ Photos ### 2026 (FINAL).jpg"))
print(clean_filename("2023-07 data analysis.xlsx"))
print(clean_filename("My Vacation Photo.jpg"))
print(clean_filename("My   Vacation   Photo.jpg"))
print(clean_filename("My @ Vacation # Photo!!.jpg"))
print(clean_filename("   Summer---Beach!!!.png   "))
print(clean_filename("Project###2026###Final.mp4"))