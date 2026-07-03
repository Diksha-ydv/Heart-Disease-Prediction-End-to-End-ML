import os 
from datetime import datetime
import logging 

log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_path = os.path.join(os.getcwd(),"logs")

os.makedirs(log_path,exist_ok=True)

log_file_path = os.path.join(log_path,log_file)

logging.basicConfig(
    filename=log_file_path,
    format='[%(asctime)s]-%(lineno)d-%(levelname)s-%(message)s',
    level=logging.DEBUG
)

if __name__=="__main__":
    logging.info("this is an info message")