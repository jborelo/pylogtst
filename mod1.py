import logging
from plog import plog

lgr = logging.getLogger(__name__)

plog(f"--- In mod1 logger name={lgr.name}, level={lgr.level}, parent logger: {str(lgr.parent)}")



def sayHi():
    ss = f"------------- m1m1m1m1 logger name: {lgr.name} level={lgr.level}, parent logger: {str(lgr.parent)}"
    plog(ss)
    lgr.debug(ss)


if __name__ == "__main__":
    lgr.info("Starting main in mod1")
    plog("Starting main in mod1")

