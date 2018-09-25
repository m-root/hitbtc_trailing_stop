import time
from datetime import datetime
import payload.payload as payload
currentTime = datetime.utcnow().strftime("%M")

def main():

    while True:
        try:
            payload.logic()

        except Exception as e:
            print(e)
            time.sleep(15)

        time.sleep(1)

    while True:
        payload.logic()

if __name__ == '__main__':
    main()