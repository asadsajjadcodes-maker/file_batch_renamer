# File Batch Renamer

A Python application designed for batch renaming files, featuring modular logging and GUI integration.

## Project Overview

This project provides a batch file renaming tool equipped with structured logging to track actions, output logs to console and file storage, and stream logs directly to the user interface.

## Features

* **Dual Logging**: Configured to write log entries to both the console and `app.log`.
* **GUI Logging Handler**: Built with PySide6 integration (`GuiHandler`) to prepare for live log displays in the user interface.

## File Structure

* `gui_handler.py` — Contains the `GuiHandler` class for processing GUI logging events.
* `main.py` — Application entry point containing logger configuration and main logic.

## Requirements & Setup

### Prerequisites

* Python 3.x
* PySide6

### Installation

1. Install required dependencies:
   ```bash
   pip install PySide6