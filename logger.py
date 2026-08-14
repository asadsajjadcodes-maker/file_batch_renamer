import logging
from gui_handler import GuiHandler

# setup logger 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
    file_handler.setLevel(logging.INFO)

    gui_handler = GuiHandler()
    gui_handler.setLevel(logging.INFO)


    console_formater = logging.Formatter(
        format = "%(asctime)s [%(levelname)s] %(message)s ",
        datefmt= "%Y-%m-%d %H:%M:%S"
    )
