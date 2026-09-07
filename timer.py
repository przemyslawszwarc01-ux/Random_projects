#Timer script

import time

wait_time = int(input("Enter how many seconds: "))

for x in range(wait_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) %60
    hours = int(x / 3600)
    print(f"{hours}:{minutes}:{seconds}")
    time.sleep(1)
print ("wake up")