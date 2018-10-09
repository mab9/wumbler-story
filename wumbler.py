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
path = "date_file"


def start_wumblering(laundry_id):
    print("laundry:", laundry_id, "has started")
    file = open(path, "a")
    file.write("laundry: " + str(laundry_id) + " has started\n")

# while True:


    for _ in range(10):
        #data.append(sensor.readAcc())
        time.sleep(0.1)
        file.write(" !\n")


def calibrate_wumbler(laundry_id):
    global calibration
    #calibration = calibrator.calibrate(laundry_id, 4)


def create_data_file(number):
    global path
    date = datetime.datetime.now()
    file_name = str(date.strftime("%Y-%m-%d")) + "-" + str(number) + str(path_postfix)

    try:
        open(file_name, 'x')
    except FileExistsError:
        create_data_file(number + 1)
    finally:
        path = file_name




# calibrateWumbler(laundry_id)
create_data_file(0)
start_wumblering(laundry_id)
