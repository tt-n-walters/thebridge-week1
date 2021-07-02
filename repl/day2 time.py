import time

seconds = 0

while seconds < 7201:
    seconds = seconds + 1

    print(seconds // 3600, ":", seconds // 60 % 60, ":", seconds % 60, "\t\t", seconds)

    time.sleep(0.001)