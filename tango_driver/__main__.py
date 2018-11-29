import threading
import os
from tango_driver import config, logger, start_http_server
from tango_driver.utils import daemon


def main():
    '''
        The main method
    '''

    # satrt daemon process
    # d = threading.Thread(target=daemon.daemon_process, name="tango-daemon", daemon=True)
    # d.start()

    logger.info("Starting server on host : %s , port : %s !",
                config.HOST, config.PORT)

    start_http_server()


'''
    The main entry point
'''

if __name__ == '__main__':
    main()
