import itertools
import time
import threading
import sys

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['.', 'o', '0', 'O']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(1)#speed of loading 0.01 is a good one
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(10000)
done = True
