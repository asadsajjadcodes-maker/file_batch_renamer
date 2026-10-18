<div align="center">

# File Batch Renamer

### Safe, Modular Desktop Bulk File Renaming & Sanitization Utility Built with Python & PySide6

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/PySide6-Qt_for_Python-41CD52?style=for-the-badge&logo=qt&logoColor=white)](https://doc.qt.io/qtforpython/)
[![CI/CD](https://img.shields.io/badge/GitHub_Actions-PyInstaller_EXE-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/asadsajjadcodes-maker/file_batch_renamer/actions)

</div>

---

**File Batch Renamer** is a modular desktop application built with **Python** and **PySide6** designed to scan, sanitize, preview, validate, and execute batch file renaming operations safely across target directories.

Instead of applying destructive file-system changes blindly, the application enforces a **Plan → Validate → Preview → Execute** pipeline with triple-channel logging (GUI console, terminal, and `app.log`).

---

## ✨ Key Features

- **Interactive Directory Selection:** Choose target folders via a native OS folder dialog (`QFileDialog`) or enter directory paths manually.
- **Deterministic Sorting & Zero-Padded Indexing:** Sorts discovered files case-insensitively and generates clean, sequential 3-digit zero-padded filenames (`<prefix>_001.ext`, `<prefix>_002.ext`, etc.).
- **Filename Sanitization Utility:** Includes regex-based filename cleaning (`cleaner.py`) that strips special characters and normalizes whitespace into underscores while preserving file extensions.
- **Pre-Execution Safety Validation:** Validates the entire rename plan before touching disk—verifying source file existence and preventing accidental destination collisions or overwrites (`validator.py`).
- **Dry-Run Live Preview:** Inspect exact `old_name -> new_name` mappings inside the read-only GUI console before executing any disk operations.
- **Triple-Channel Logging Architecture:** Routes runtime events simultaneously to:
  1. **GUI Console (`QTextEdit`)** via a custom Qt `Signal(str)` logging bridge (`GuiHandler`)
  2. **Persistent Log File (`app.log`)** with module, function, and line-number diagnostics
  3. **Standard Output Console (`StreamHandler`)**
- **Automated Windows Executable Packaging (CI/CD):** Includes a GitHub Actions workflow (`.github/workflows/build.yml`) that automatically builds a standalone Windows executable using `PyInstaller` on every push to `main`.

---

## 🔄 Execution Pipeline

```text
Select Target Directory & Prefix
               ↓
   Scan & Case-Insensitive Sort (scanner.py)
               ↓
   Generate Sequential Rename Plan (renamer.py)
               ↓
   Validate Source & Collision Safety (validator.py)
               ↓
   ├── [Preview Mode] → Stream Proposed Plan to GUI Console
   └── [Rename Mode]  → Execute Atomic Renames on Disk (executor.py)
```

---

## 📂 Project Structure

```text
file_batch_renamer/
├── .github/
│   └── workflows/
│       └── build.yml       # GitHub Actions CI workflow (PyInstaller Windows EXE build)
├── app/
│   ├── main.py             # PySide6 desktop GUI window & event controllers
│   ├── scanner.py          # Recursive pathlib file discovery utility
│   ├── cleaner.py          # Regex filename sanitization helper
│   ├── renamer.py          # Zero-padded sequential rename plan generator
│   ├── validator.py        # Pre-execution path & overwrite collision validator
│   ├── executor.py         # File-system rename execution engine
│   ├── preview.py          # CLI/text preview formatting utility
│   ├── gui_handler.py      # Custom QObject + logging.Handler Qt signal bridge
│   └── logger.py           # Centralized triple-handler logging configuration
├── .gitattributes
├── .gitignore
└── README.md
```

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ | Core application logic |
| **Desktop GUI** | PySide6 (Qt for Python) | Desktop interface, widgets, dialogs, and signals |
| **File System** | `pathlib` | Cross-platform path manipulation and recursive scanning |
| **Text Processing** | `re` (Regular Expressions) | Filename sanitization and character normalization |
| **Diagnostics** | `logging` | Multi-destination telemetry (GUI, file, console) |
| **Packaging & CI** | PyInstaller & GitHub Actions | Automated Windows `.exe` artifact generation |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/asadsajjadcodes-maker/file_batch_renamer.git
cd file_batch_renamer
```

### 2. Create a Virtual Environment & Install Dependencies

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

pip install PySide6
```

### 3. Run the Application

```bash
python app/main.py
```

---

## 📖 Usage Guide

1. **Select Directory:** Click **Browse** to pick a target folder using the native folder dialog, or paste a directory path into the input field.
2. **Define Prefix:** Enter your desired filename prefix (e.g., `asset`, `invoice`, `photo`) in the **Prefix** field.
3. **Preview Changes (Dry Run):** Click **Preview** to validate the plan and inspect the proposed `source -> destination` mappings in the live log console without modifying any files.
4. **Execute Batch Rename:** Click **Rename** to apply the validated rename plan across the target directory.

---

## 👤 Author

**Asad Sajjad**
- GitHub: [@asadsajjadcodes-maker](https://github.com/asadsajjadcodes-maker)
