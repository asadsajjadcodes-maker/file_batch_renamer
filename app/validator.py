from pathlib import Path

def validate_rename_plan(plan: list[tuple[Path, Path]]) -> list[str]:

    """
    Validate a rename plan.

    Returns a list of error messages.
    """

    errors = []
    # storing the old file names in source_paths as a set 
    # _ is to ignore the second velue in plan list 
    source_paths = {source.resolve() for source, _ in plan}

    for source, destination in plan:
        if not source.exists():
            errors.append(f"Source path {source} does not exist.")



        destination_path = destination.resolve()
        if (destination_path.exists() and destination_path not in source_paths):
            errors.append(f"Destination path {destination} already existed.")

    return errors

