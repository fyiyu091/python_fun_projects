import time as t
import logging as log

def main():
    print(t.time())
    t.sleep(1)
    #Thred_time doesn't including the sleep time
    print(t.thread_time())

    log.basicConfig(filename='log_examples.txt', level=log.WARNING)
    #level from bottom to top
    log.debug('debug info')
    log.info('info info')
    log.warning('warning info')
    log.error('error info')
    log.critical('critical info')

if __name__ == "__main__":
    main()