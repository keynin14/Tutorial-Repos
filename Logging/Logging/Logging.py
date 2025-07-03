import logging

logging.basicConfig(level=logging.DEBUG)

# logging.info("You have got 20 mails in your inbox")
# logging.critical("All components failed!")

logger=logging.getLogger("NenuralNine Logger")
# logger.info("The best logger was just created!")
# logger.critical("Your YouTube channel was deleted!")
# logger.log(logging.ERROR,"An error occured!")

logger.setLevel(logging.DEBUG)

handler=logging.FileHandler("mylog.log")
handler.setLevel(logging.INFO)

formatter=logging.Formatter("%(levelname)s - %(asctime)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("This is a debug message!")
logger.info("This is important information!")

