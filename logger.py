import logging
LOG_PATH = 'logs/SavageGardenBotLog.txt'
logging.basicConfig(level=logging.INFO, filename=LOG_PATH,
    format='%(asctime)s: %(message)s', datefmt='%b %d %T')
def log(logmessage):
    logging.info(logmessage)