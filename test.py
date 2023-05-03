from tqdm import tqdm
from time import sleep
import threading

nums = 0
fnums = 294

def progress_bar():
    global nums, fnums
    for int in tqdm(range(fnums)):
        olnum = nums
        while True:
            if not nums == olnum:
                break
            continue
g = 1
threading.Thread(target=progress_bar).start()
sleep(5)
while True:
    sleep(0.1)
    g = g * 2
    nums += 1
    if nums == fnums:
        break