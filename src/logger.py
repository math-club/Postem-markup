import logging


logger = logging.getLogger("Postem logger")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s :: %(message)s')
file_handler = logging.FileHandler("output.log")


file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
