import logging


logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

fh = logging.FileHandler('logs.log', 'a')
fh.setLevel(logging.DEBUG)

logger.addHandler(sh)
logger.addHandler(fh)

formatter = logging.Formatter("[%(asctime)s][%(levelname)s] %(filename)s : %(message)s")
sh.setFormatter(formatter)
fh.setFormatter(formatter)