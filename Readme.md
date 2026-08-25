# File Batch Renamer

A lightweight desktop application built with Python and PySide6 designed to scan, preview, validate, and execute batch file renaming operations safely across directories.

## Features

- **Directory Scanning**: Recursively scans target folders for files using pattern matching.
- **Custom Prefixing & Numbering**: Generates structured 3-digit zero-padded index numbers (`001`, `002`, etc.) with user-defined prefixes.
- **Filename Sanitization**: Strip unwanted special characters and replace spaces with underscores while preserving file extensions.
- **Safety Validation**: Validates paths prior to execution to prevent accidental overwrites or missing file errors.
- **Dry-Run Preview**: Inspect planned file structure changes in the console before applying changes to disk.
- **Graphical Interface**: Clean GUI powered by PySide6.

## Project Structure

```text
file_batch_renamer/
├── app/
│   ├── __init__.py
│   ├── cleaner.py      # Filename sanitization logic
│   ├── executor.py     # System file operation execution
│   ├── gui.py          # PySide6 desktop user interface
│   ├── preview.py      # Preview formatting logic
│   ├── renamer.py      # Rename plan generation
│   ├── scanner.py      # File system search utility
│   └── validator.py    # Pre-execution validation checks
├── Images/
├── .gitignore
└── Readme.md