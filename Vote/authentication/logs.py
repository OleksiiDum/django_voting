import logging


logger = logging.getLogger("authentication")
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

fh = logging.FileHandler('logs.log', 'a')
fh.setLevel(logging.DEBUG)

logger.addHandler(sh)
logger.addHandler(fh)