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

'''
   ======================= Sell trail stop ========================

   [6466.85, 6464.11, 6464.0, 6462.12, 6462.04, 6461.66]

   ================================================================

   6466.98

   ======================= Buy trail stop =========================

   [6468.3, 6468.66, 6471.03, 6472.24, 6473.59, 6475.24, 6475.81, 6476.02, 6476.52, 6476.68, 6477.93, 6479.95, 6483.68]

   ================================================================
'''
