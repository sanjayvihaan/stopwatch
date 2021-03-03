import time
print("Press Enter key to start")
print("press ctrl+C to stop the timer")

while True:
    try:
        input()
        start = time.time()
        print("started")
    except KeyboardInterrupt:
        print("Stoped")
        end = time.time()
        print("Total time: ", round(end-start,2),"seconds")
        break


