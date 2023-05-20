import os
import pandas as pd
import time
from datetime import datetime


def computeRate(hrs, type):
    perHour = 10
    baseRate = 0
    if(type == 2):
        baseRate = 40
    elif(type == 1):
        baseRate = 20
    elif(type == 0):
        baseRate = 0
        perHour = 0

    if hrs >= 4:
        return ((hrs - 4) * perHour) + baseRate
    else:
        return baseRate


def inputCheck():
    while True:
        os.system('clear')
        print(df)
        a = input("Enter index no or type exit: ")
        try:
            ans = int(a)
            if 0 <= ans < df.shape[0]:
                return ans
            else:
                print("Entry not found")
                time.sleep(1)
        except:
            if a.lower() == 'exit':
                print('[INFO] Saving ', fname)
                time.sleep(0.5)
                print('[INFO] Exiting Program')
                time.sleep(1)
                df.to_csv(fname, index=False)
                exit()
            else:
                print("Invalid input")
                time.sleep(1)
# check for file



fname = 'Vehicle Log.csv'
if os.path.exists(fname):
    df = pd.read_csv(fname)
    print('[INFO] Opening File')
else:
    print('[INFO] File does not exist')
    print('[INFO] Exiting Program')
    time.sleep(1)
    exit()

now = datetime.now()
now = now.strftime("%m/%d/%Y, %H:%M:%S")

while True:
    os.system('clear')
    time.sleep(1)
    ans = inputCheck()
    currLog = df.iloc[ans]
    pastTime = currLog['Time In']
    stay = datetime.strptime(now, "%m/%d/%Y, %H:%M:%S") - datetime.strptime(pastTime, "%m/%d/%Y, %H:%M:%S")
    if currLog['Checked In'] == 0:
        print("Vehicle has already been checked out")
        time.sleep(1)
        continue
    hrs = stay.total_seconds() // 3600
    print(computeRate(hrs, currLog['Vehicle Type']))
    b = input('Pay? Y/N: ')
    if b.lower() == 'y':
        df.iat[ans, 3] = 0
        df.iat[ans, 1] = now
        print('Paid!')
        time.sleep(1)
    else:
        print('Not paid')
        time.sleep(1)
