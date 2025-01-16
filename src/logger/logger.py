import logging
import os

from datetime import datetime
FILE_PATH = os.path.join(os.getcwd(),'Logs')
os.makedirs(FILE_PATH,exist_ok=True)
PATH_LOGS = os.path.join(os.getcwd(),'Logs','log.log')


logging.basicConfig(filename=PATH_LOGS,
                    filemode='w',
                    format='%(asctime)s---%(name)s--%(lineno)d --%(levelname)s--%(message)s',
                    level=logging.INFO)


