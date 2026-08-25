from pathlib import Path


def execute_rename_plan(plan: list[tuple[Path,Path]]) -> None:
    """
    Execute the rename plan , rename the files in system 
    """

    for source, destination in plan:
        source.rename(destination)
        