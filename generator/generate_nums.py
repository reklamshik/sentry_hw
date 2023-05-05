import threading
import random
import time
import requests
from loguru import logger

def get_nums():
    return random.randint(0, 15), random.randint(0, 8)


def run():
    while True:
        try:
            requests.get("http://division:5000/division?first=%s&second=%s" % get_nums())
            logger.info('GET div')
        except:
            logger.info('Error')
        time.sleep(1)

if __name__ == '__main__':
    for _ in range(2):
        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()
        
    while True:
        time.sleep(2)
        