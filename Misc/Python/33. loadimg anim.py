import itertools
import threading
import sys
import time

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['.', '..', '...', '....']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)#speed of loading 0.01 is a good one
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(0.8)
done = True

print()
print("Done!")
