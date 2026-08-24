from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QLabel,
    QLineEdit,
    QCheckBox
)
from pathlib import Path
from scanner import find_files
from renamer import create_rename_plan
from validator import validate_rename_plan


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
        self.folder_input.setPlaceholderText("Enter folder path")

        # text input box for an optional prefix for renamed files.
        self.prefix_input = QLineEdit()
        self.prefix_input.setPlaceholderText("Prefix")

        # checkbox for file name cleaning 
        self.clean_checkbox = QCheckBox(
            "Clean Filename"
        )

        # preview button 
        self.preview_button = QPushButton("Preview")

        # rename button
        self.rename_button = QPushButton("Rename")
        
        # connect preview button
        self.preview_button.clicked.connect(self.preview)









        # add all widgets to the vertical layout top to bottom

        layout.addWidget(title)
        layout.addWidget(self.folder_input)
        layout.addWidget(self.prefix_input)
        layout.addWidget(self.clean_checkbox)
        layout.addWidget(self.preview_button)
        layout.addWidget(self.rename_button)

        # apply the layout configuration to the main window.
        self.setLayout(layout)  # set the layout to the main window

    # preview function 
    def preview(self):
        folder = self.folder_input.text() # collects data from folder input box.
        prefix = self.prefix_input.text() # collects data from prefix input box.

        files = find_files(folder)
        files = sorted(files, key=lambda file: file.name.lower()) # sort the file list using lowercase file names 

        plan = create_rename_plan(files, prefix)

        errors = validate_rename_plan(plan)

        if errors:
            for error in errors:
                print(f"Error: {error}")
            return

        for source, destination in plan:
            print(f"{source.name} ->  {destination.name}")



        




app = QApplication([])
window = MainWindow()
window.show()
app.exec()
