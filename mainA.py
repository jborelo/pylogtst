import logging
from plog import  plog

import mod1 as m1
import mod2 as m2



lgr = logging.getLogger(__name__)
plog(f"--- In modA before  config logger name={lgr.name}, level={lgr.level}, parent logger: {str(lgr.parent)}")

logging.basicConfig(format='%(asctime)s : %(name)s.%(funcName)s(): %(message)s', level=logging.DEBUG)

plog(f"--- In modA after  config logger name={lgr.name}, level={lgr.level}, parent logger: {str(lgr.parent)}")


if __name__ == "__main__":
    plog (f"In modA name of logger: {lgr.name}, level: {lgr.level}, parent: {str(lgr.parent)}")
    lgr.debug(f"log from modA  name of logger: {lgr.name}, level: {lgr.level}, parent: {str(lgr.parent)}")
    m1.sayHi()
    m2.sayHi()
