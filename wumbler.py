#!/usr/bin/env python3

import time
import uuid

import calibrator
import sensor

#https://mlhub.cs.technik.fhnw.ch/user/marcantoine.bruelhart/lab - rQ3nzu

laundryId = uuid.uuid4()
calibration = None
dataPath = "datum.wd"


def startWumblering(laundryId):
    print("laundry: ", laundryId, " has started")
    file = open(dataPath, "a")

    while True:
        data = [laundryId, "&"]

        for _ in range(10):
            data.append(sensor.readAcc())
            data.append("&")
            time.sleep(0.1)

        file.write("Now the file has one more line!")



def calibrateWumbler(laundryId):
    global calibration
    calibration = calibrator.calibrate(laundryId, 4)


#calibrateWumbler(laundryId)
startWumblering(laundryId)
