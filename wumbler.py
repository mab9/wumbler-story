#!/usr/bin/env python3

import time
import uuid
import datetime

#import calibrator
#import sensor

# https://mlhub.cs.technik.fhnw.ch/user/marcantoine.bruelhart/lab - rQ3nzu

laundry_id = uuid.uuid4()
calibration = None
path_postfix = ".wd"
path="date_file"


def start_wumblering(laundry_id):
    print("laundry:", laundry_id, "has started")
    file = open(path, "a")

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


def create_data_file(start):
    number = start
    global path
    try:
        date = datetime.datetime.now()
        file_name = str(date.strftime("%Y-%m-%d"))
        file_name += "_" + str(number) + str(path_postfix)
        open(file_name, 'x')
        path = file_name
    except FileExistsError:
        number += 1
        create_data_file(number)




# calibrateWumbler(laundry_id)
create_data_file(0)
start_wumblering(laundry_id)
