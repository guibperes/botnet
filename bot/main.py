from env import Env
from logger import logger_init
from request_thread import RequestThread

def main():
    env = Env()
    logger_init()

    RequestThread.start_many(RequestThread.create_many(
        quantity=env.get('threads'),
        url=env.get('url')
    ))


main()
