from pathlib import Path

# cleans the file name 
def clean_filename(filename : str) ->str:

    path = Path(filename).resolve()

    stem = path.stem
    ex = path.suffix

    stem = stem.strip()
    stem = stem.replace(" ", "_")
    return stem + ex

