from pathlib import Path

def preview_rename_plan(plan: list[tuple[Path, Path]]) -> None:
    """
    Prints a preview of the rename plan.
    """
    for source, destination in plan:
        print(f"Preview: {source.name} -> {destination.name}")


