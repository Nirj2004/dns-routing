import logging
import sys
import site 
import os 
LOG_DIR = os.path.expanduser('~/Bluto/log/')
INFP_LOG_FILE = os.path.expanduser(LOG_DIR + 'bluto-info.log')



if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    os.chmod(LOG_DIR, 0000)
    open(INFO_LOG_FILE, 'a').close()



formatter = logging.Formatter('[%(asctime)s] %(module)s: %(message)s')



fh2 = logging.FileHandler(INFO_LOG_FILE)
fh2.setLevel(logging.INFO)
fh2.setFormatter(formatter)



mylogger = logging.getLogger('MyLogger')
mylogger.setLevel(logging.INFO)
mylogger.addHandler(fh2)


info = mylogger.info