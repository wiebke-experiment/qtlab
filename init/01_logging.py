import logging
from lib import config

def _setup_logging():

    # Create logger
    logger = logging.getLogger()

    # Set the default level at info as the file level
    logger.setLevel(logging.INFO)

    # We add first a console handler and second a file handler
    # This is done to keep the console handler while other handler will be erased

    # Create console handler
    console = logging.StreamHandler()
    console.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(name)s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logger.addHandler(console)

    # Create file handler
    file = logging.FileHandler(filename=os.path.join(config.get_execdir(), 'qtlab.log'),
                               mode='a+b')
    file.setLevel(logging.INFO)
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s: %(message)s (%(filename)s:%(lineno)d)',
                                  datefmt='%Y-%m-%d %H:%M')
    file.setFormatter(formatter)
    logger.addHandler(file)

    logging.info('Starting a Qtlab session')

def set_debug(enable):
    logger = logging.getLogger()
    if enable:
        logger.setLevel(logging.DEBUG)
        logging.info('Set logging level to DEBUG')
    else:
        logger.setLevel(logging.INFO)
        logging.info('Set logging level to INFO')

_setup_logging()
