import logging
import os
from datetime import datetime

'''
Logger is used to track and record any execution. It captures detailed 
information about any errors or events (what the happens). The purpose is 
monitoring and troubleshooting issues by reviewing th elogs.
'''
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO # print the spesific messages, to put it inside the file
)

if __name__ == "__main__":
    logging.info("Logging has started")