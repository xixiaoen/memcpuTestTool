import logging
import os
import Constant

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
if not os.path.exists(Constant.LOG_PAHT):
    os.makedirs(Constant.LOG_PAHT)
fh = logging.FileHandler(os.path.join(Constant.LOG_PAHT, r'log.txt'))
fh.setLevel(logging.INFO)
fh_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(fh_formatter)
logger.addHandler(fh)
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
sh_formatter = logging.Formatter('%(message)s')
sh.setFormatter(sh_formatter)
logger.addHandler(sh)
