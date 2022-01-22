import logging

logging.basicConfig(filename = "logfile4.txt",level = logging.ERROR,format = '%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start the program')

def func1(a,b):
    logging.debug('Entered into the func1')
    logging.debug('arguments passed'+str(a)+'and'+str(b))
    if b==0:
        logging.critical("Second arguments is zero")
        raise Exception("second argument must not be zero")
    logging.info("Going to execute division")
    div = a/b
    logging.info("Division got executed successfully")
    logging.warning("Returning the value"+str(div))
    return div

func1(100,5)
