import sys
import getopt
import requests
import threading
import logging

class RequestThread(threading.Thread):
    def __init__(self, id, url):
        threading.Thread.__init__(self)

        self.id = id + 1
        self.name = 'RequestThread'
        self.url = url

        logging.info(f'Creating thread {self.name} with id {self.id}')
    
    def run(self):
        logging.info(f'Starting thread {self.id}')

        response = requests.get(self.url)

        logging.info(f'Finished thread {self.id} with response status {response.status_code}')
    
    @staticmethod
    def create_many(quantity, url):
        return list(map(lambda i: RequestThread(i, url), range(quantity)))
    
    @staticmethod
    def start_many(threads):
        for thread in threads:
            thread.start()

def main():
    logging.basicConfig(format='%(process)s [%(levelname)s] (%(asctime)s) %(threadName)s - %(message)s', level=logging.INFO)

    options = dict(getopt.getopt(args=sys.argv[1:], shortopts='t:u:')[0])

    RequestThread.start_many(RequestThread.create_many(quantity=int(options.get('-t')), url=options.get('-u')))

main()
