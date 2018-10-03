from datetime import datetime
import time;
import random;

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31 ]

for i in range(7):
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print("This minute is a little odd")
    else:
        print("Not an odd minute")

    print("We will wait for: ")
    time_to_sleep = random.randint(1,60)
    print(time_to_sleep)
    time.sleep(time_to_sleep)

print("DONE")
