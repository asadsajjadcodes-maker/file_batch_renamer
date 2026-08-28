# File Batch Renamer

A desktop application built with Python and PySide6 designed to scan, preview, validate, and execute batch file renaming operations safely across target directories.

## Features

- **Interactive Directory Picker**: Select target folders via a native file dialog using the **Browse** button or enter path strings manually.
- **Input Validation**: Guard clauses ensure mandatory fields (Folder Path & Prefix) are populated before previewing or executing tasks.
- **Custom Prefixing & Indexing**: Generates structured 3-digit zero-padded index numbers (`001`, `002`, etc.) combined with user-defined prefixes.
- **Filename Sanitization**: Strips unwanted special characters and replaces spaces with underscores while preserving file extensions.
- **Safety Validation**: Validates paths prior to execution to prevent accidental overwrites or missing file errors.
- **Dry-Run Preview**: Inspect planned file structure changes inside the live GUI console before applying changes to disk.
- **Integrated Real-time Logging**: Custom signal handlers route log outputs directly to the UI display screen, application log file (`app.log`), and console.

## Project Structure

```text
file_batch_renamer/
├── app/
│   ├── cleaner.py      # Filename sanitization logic
│   ├── executor.py     # System file operation execution
│   ├── gui_handler.py  # PySide6 custom logging signal handler
│   ├── logger.py       # Centralized logging configuration
│   ├── main.py         # PySide6 desktop interface entry point
│   ├── preview.py      # Preview formatting utility
│   ├── renamer.py      # Rename plan generation module
│   ├── scanner.py      # File system search utility
│   └── validator.py    # Pre-execution validation checks
├── Images/
├── .gitignore
└── Readme.md




### Setup and running 

Clone Repository:
git clone [https://github.com/asadsajjadcodes-maker/file_batch_renamer.git](https://github.com/asadsajjadcodes-maker/file_batch_renamer.git)
cd file_batch_renamer

Install Dependencies:
pip install PySide6

Run Application:
python app/main.py



Workflow Guide

  1.  Select Directory: Click Browse to choose a target folder via the file picker, or type/paste the directory path manually into the path input.

  2.  Define Prefix: Enter your desired prefix into the prefix input box.

  3.  Preview: Click Preview to review proposed file name mappings in the live log screen.

  4.  Rename: Click Rename to execute the changes across disk.

