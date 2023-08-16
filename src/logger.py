import logging
import os
import sys
from datetime import datetime
from exception import CustomException

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(),'logs')

os.makedirs(logs_path, exist_ok=True)

log_file_path = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
     filename = log_file_path,
     level = logging.INFO,
     format = '[ %(asctime)s ] %(lineno)d - %(name)s - %(levelname)s - %(message)s'    
)


if __name__ == '__main__':
    try:
        a = 10/0
    except Exception as e:
        logging.error('Logging started')
        raise CustomException(e, sys)