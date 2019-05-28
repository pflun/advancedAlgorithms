import time
starttime=time.time()
while True:
  print "tick"
  time.sleep(3.0 - ((time.time() - starttime) % 3.0))