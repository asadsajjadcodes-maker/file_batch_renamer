from PySide6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QWidget, 
    QVBoxLayout,
    QHBoxLayout, 
    QLabel, 
    QPushButton, 
    QLineEdit, 
    QTextEdit, 
    QFileDialog,
    QProgressBar
)
from pathlib import Path
from scanner import find_files
from renamer import create_rename_plan
from validator import validate_rename_plan
from executor import execute_rename_plan
from logger import log_info, log_warning, log_error, gui_handler

class MainWindow(QWidget):
    def __init__(self):
        # call the constructor of the parent class QWidget 
        super().__init__()

        # set window title and size
        self.setWindowTitle("File Batch Renamer")
        self.resize(700, 600)

        self.build_ui()  # it will create all the widgets and layout

    def build_ui(self):
        # create a vertical layout to arrange widgets top to bottom.
        layout = QVBoxLayout()

        # create a main heading label
        title = QLabel("Batch Rename Files")


        # Text input box for the target directory 
        self.folder_input = QLineEdit()
        self.folder_input.setPlaceholderText("Enter folder path or clisk 'Browse' to select a folder.")

        # text input box for an optional prefix for renamed files.
        self.prefix_input = QLineEdit()
        self.prefix_input.setPlaceholderText("Prefix")


       
        # browse button 
        self.browse_button = QPushButton("Browse")

        # preview button 
        self.preview_button = QPushButton("Preview")

        # rename button
        self.rename_button = QPushButton("Rename")
        
        # connect preview button
        self.preview_button.clicked.connect(self.preview)

        # connect rename button.
        self.rename_button.clicked.connect(self.rename)

        # connect browse button 
        self.browse_button.clicked.connect(self.browse_folder)







        # add all widgets to the vertical layout top to bottom

        layout.addWidget(title)
        layout.addWidget(self.folder_input)
        layout.addWidget(self.prefix_input)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.preview_button)
        layout.addWidget(self.rename_button)

        # apply the layout configuration to the main window.
        self.setLayout(layout)  # set the layout to the main window

        # Log Text Area
        self.display_screen = QTextEdit()
        self.display_screen.setReadOnly(True)
        layout.addWidget(self.display_screen)

        # Connect shared GUI handler signal to display_screen writer method
        gui_handler.log_message.connect(self.show_message)
        log_info("GUI triple-logging system initialized successfully.")


    def browse_folder(self):
        # open folder picker dialog and set selected directory Path.

        selected_folder = QFileDialog.getExistingDirectory(self, "Select Asset Directory", "")

        if selected_folder:
            self.folder_input.setText(selected_folder)
            log_info(f"Folder selected : '{selected_folder}'")












    def show_message(self, message: str) -> None:
        """Appends formatted messages directly to the UI screen."""
        self.display_screen.append(message)

    # preview function 
    def preview(self):
        folder = self.folder_input.text() # collects data from folder input box.
        prefix = self.prefix_input.text() # collects data from prefix input box.
        if not folder or not prefix:
            log_error("Error : Folder path and prefix can not be empty!")
            return

        files = find_files(folder)
        files = sorted(files, key=lambda file: file.name.lower()) # sort the file list using lowercase file names 

        plan = create_rename_plan(files, prefix)

        errors = validate_rename_plan(plan)

        if errors:
            for error in errors:
                log_info(f"Error: {error}")
            return

        for source, destination in plan:
            log_info(f"{source.name} ->  {destination.name}")


    def rename(self):
        folder = self.folder_input.text()
        prefix = self.prefix_input.text()

        if not folder or not prefix:
            log_error("Error : Folder path and prefix can not be empty!")
            return

        files = find_files(folder)
        files = sorted(files, key=lambda file: file.name.lower())
        plan = create_rename_plan(files,prefix)

        errors = validate_rename_plan(plan)
        if errors:
            for error in errors:
                log_info(f"Error: {error}")
            return
        else:
            execute_rename_plan(plan)
            for source, destination in plan:
                log_info(f"Renamed : {source.name} -> {destination.name}")


        log_info("Task completed successfully")
                    




app = QApplication([])
window = MainWindow()
window.show()
app.exec()