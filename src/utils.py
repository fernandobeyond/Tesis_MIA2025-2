"""utils.py
Logging helper
"""
import logging
def setup_logging(path=None):
    if path:
        logging.basicConfig(filename=path, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    else:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    return logging.getLogger()
