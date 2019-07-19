import time as t
import logging as log
from datetime import datetime as dt

def main():

    log.basicConfig(filename='log_examples.txt', level=log.WARNING)
    #level from bottom to top
    log.debug('debug info')
    log.info('info info')
    log.warning('warning info')
    log.error('error info')
    log.critical('critical info')

    log_message('pass here')
    t.sleep(1)
    log_message('fail there', time=dt.utcnow())

def log_message(msg, *, time=None):
    if not time:
        time = dt.utcnow()
    print(msg, f'the time is {time}')


if __name__ == "__main__":
    main()