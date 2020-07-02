import logging

def logger_init():
    logging.basicConfig(format='%(process)s [%(levelname)s] (%(asctime)s) %(threadName)s - %(message)s', level=logging.INFO)
