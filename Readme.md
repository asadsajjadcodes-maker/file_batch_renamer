# File Batch Renamer

A desktop application built with Python and PySide6 designed to scan, preview, validate, and execute batch file renaming operations safely across directories.

## Features

- **Directory Scanning**: Recursively scans target folders for files using pattern matching.
- **Input Validation**: Guard clauses verify folder path and prefix inputs before executing any actions.
- **Custom Prefixing & Numbering**: Generates structured 3-digit zero-padded index numbers (`001`, `002`, etc.) with user-defined prefixes.
- **Filename Sanitization**: Strips unwanted special characters and replaces spaces with underscores while preserving file extensions.
- **Safety Validation**: Validates paths prior to execution to prevent accidental overwrites or missing file errors.
- **Dry-Run Preview**: Inspect planned file structure changes before applying them to disk.
- **Integrated Logging System**: Features direct GUI logging via custom signal handlers alongside standard file (`app.log`) and console output logging.
- **Graphical Interface**: Clean GUI powered by PySide6 with real-time log output feedback.

## Project Structure

```text
file_batch_renamer/
├── cleaner.py      # Filename sanitization logic
├── executor.py     # System file operation execution
├── gui_handler.py  # PySide6 custom logging signal handler
├── logger.py       # Centralized logging configuration (Console, File, GUI)
├── main.py         # Application entry point and PySide6 user interface
├── preview.py      # Preview formatting logic
├── renamer.py      # Rename plan generation
├── scanner.py      # File system search utility
├── validator.py    # Pre-execution validation checks
├── Images/
├── .gitignore
├── app.log
└── Readme.md
