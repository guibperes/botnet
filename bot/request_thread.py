from threading import Thread
import logging
import requests

class RequestThread(Thread):
    def __init__(self, id, url):
        Thread.__init__(self)

        self.id = id + 1
        self.name = 'RequestThread'
        self.url = url
        self.logger = logging.getLogger()

        self.logger.info(f'Creating thread {self.name} with id {self.id}')
    
    def run(self):
        self.logger.info(f'Starting thread {self.id}')

        response = requests.get(self.url)

        self.logger.info(f'Finished thread {self.id} with response status {response.status_code}')
    
    @staticmethod
    def create_many(quantity, url):
        return list(map(lambda i: RequestThread(i, url), range(quantity)))
    
    @staticmethod
    def start_many(threads):
        for thread in threads:
            thread.start()