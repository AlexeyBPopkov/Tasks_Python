import threading
import time

def clock(name):
    print(f"Thread {name} started!")
    for i in range(10,0,-1):
        print(f"Thread {name} => {i}\t")
        time.sleep(1)
    print(f"Thread {name} finished!\t")

t1 = threading.Thread(target=clock, args=(1,))
t2 = threading.Thread(target=clock, args=(2,))
t1.daemon = True
t2.daemon = True
t1.start()
t2.start()
t1.join()
t2.join()