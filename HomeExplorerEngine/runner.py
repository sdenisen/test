import time
from HomeExplorerEngine.EngineController import EngineController

__author__ = 'sdeni'
# empty integration..

ec = EngineController()

ec.goForward()
time.sleep(5)
ec.stop()
time.sleep(5)
ec.goBackward()
time.sleep(5)


ec.stop()
time.sleep(1)
print "stop - all - motors"
ec.cleanup()