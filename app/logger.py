import logging
from gui_handler import GuiHandler

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)


if not logger.handlers:


    # console handler 
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # file handler
    file_handler = logging.FileHandler("app.log", mode= "a", encoding="utf-8")
    file_handler.setLevel(logging.INFO)

    # gui handler 
    gui_handler = GuiHandler()
    gui_handler.setLevel(logging.INFO)


    # set formats

    console_formatter = logging.Formatter(
        fmt= "%(asctime)s [%(levelname)s] - %(message)s",
        datefmt= "%Y-%m-%d %H:%M:%S"
    )


    file_formatter = logging.Formatter(
        fmt= "%(asctime)s [%(levelname)s] [%(filename)s]:%(funcName)s:%(lineno)d - %(message)s",
        datefmt= "%Y-%m-%d %H:%M:%S"
    )

    gui_formatter = logging.Formatter(
        fmt="%(levelname)s - %(message)s"
    )


    # attach formatters to the handlers 
    console_handler.setFormatter(console_formatter)
    file_handler.setFormatter(file_formatter)
    gui_handler.setFormatter(gui_formatter)

    # attach handlers to start logging 

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.addHandler(gui_handler)




def log_info(message: str) -> None:
    logger.info(message)

def log_warning(message: str) -> None:
    logger.warning(message)

def log_error(message: str) -> None:
    logger.error(message)


