from config.env import Env
from config.logger import logger_init
from thread.request_thread import RequestThread

def main():
    env = Env()
    logger_init()

    RequestThread.start_many(RequestThread.create_many(
        quantity=env.get('threads'),
        url=env.get('url')
    ))

main()
