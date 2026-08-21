# File Batch Renamer

A Python-based CLI tool designed to recursively scan directories and safely sanitize file names by removing special characters, normalizing spacing, and converting text to lowercase while preserving file extensions.

---

## 🛠️ Features & Progress

* **Day 1–2: String Sanitization (`cleaner.py`)**
  * Strips leading and trailing whitespace[cite: 1].
  * Replaces special characters, symbols, and spaces with single underscores (`_`)[cite: 1].
  * Normalizes file stems to lowercase while retaining original file extensions[cite: 1].

* **Day 3: Recursive Directory Scanner (`scanner.py`)**
  * Uses `pathlib.Path` to scan directories recursively via `rglob`[cite: 2].
  * Accepts custom wildcard pattern matching (e.g., `*.py`, `*.jpg`)[cite: 2].
  * Validates path existence and safely returns lists of target files[cite: 2].

---

## 📂 Project Structure

```text
file_batch_renamer/
│
├── app/
│   ├── __init__.py    # Package initialization module
│   ├── cleaner.py     # Core logic for string and filename sanitization
│   └── scanner.py     # Directory scanning and file discovery module
│
└── README.md          # Project documentation