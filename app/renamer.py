from pathlib import Path

def create_rename_plan(files, prefix):
    """
    Plan a file rename operation by returning a list of tuples,
      where each tuple contains the old and new file paths."""

    plan = []
    for number, file in enumerate(files, start=1):
        file = Path(file)
        
      
        new_name = f"{prefix}_{number:03d}{file.suffix}"
        new_name = file.with_name(new_name)
        plan.append((file, new_name))
    return plan



