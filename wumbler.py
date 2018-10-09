#!/usr/bin/env python3

import time
import uuid

#import calibrator
#import sensor

# https://mlhub.cs.technik.fhnw.ch/user/marcantoine.bruelhart/lab - rQ3nzu

laundry_id = uuid.uuid4()
calibration = None
data_path = "datum.wd"


def start_wumblering(laundry_id):
    print("laundry:", laundry_id, "has started")
    file = open(data_path, "a")

    # while True:
    data = [laundry_id, "&"]

    for _ in range(10):
        #data.append(sensor.readAcc())
        data.append("&")
        time.sleep(0.1)
        file.write("Now the file has one more line!\n")


def calibrate_wumbler(laundry_id):
    global calibration
    #calibration = calibrator.calibrate(laundry_id, 4)


# calibrateWumbler(laundry_id)
start_wumblering(laundry_id)
