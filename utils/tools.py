import logging
import sys

def getlogger():

    """
    Function getlogger gives the default logger to log the messages.

    """

    LOGGER=None
    if LOGGER is None:
        LOGGER = logging.getLogger('producer')
        if len(LOGGER.handlers)==0:
            LOGGER.addHandler(logging.StreamHandler(sys.stdout))
            LOGGER.setLevel(logging.DEBUG)
    return LOGGER

def convert(string):

    """
    Function convert convert the given string of the type 2017-07-15 02:40:17 into datetime format.

    """

    y=int(string[0:4])
    m = int(string[5:7])
    d = int(string[8:11])
    h = int(string[11:13])
    mm = int(string[14:16])
    ss = int(string[17:19])

    return datetime.datetime(y, m, d, h, mm, ss)


def get_epoch(dt):

    """
    Function get_epoch converts the given datetime into the epoch timestamp.

    """

    return int((dt - datetime.datetime(1970,1,1)).total_seconds())


def writetofile(data):

    """
    Function writetofile writes the given data into a file.

    """

    f = open("Violateddata.txt", "a")
    f.write("{0}\n".format(data))





