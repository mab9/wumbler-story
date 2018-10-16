#!/usr/bin/env python3

import time
import uuid
import datetime
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
    file.write("x, y, z coordinates\n")

# while True:
    for _ in range(10):
        # data.append(sensor.readAcc())
        data = []
        #data.append("bla")
        #data.append("bla")
        file.write(", " . join(data) + "\n")
        #time.sleep(0.1)
    file.close()


def create_data_file(number):
    global path
    date = datetime.datetime.now()
    file_name = str(date.strftime("%Y-%m-%d")) + "-" + str(number) + str(path_postfix)

    try:
        file = open(file_name, 'x')
        file.close()
        path = file_name
    except FileExistsError:
        increment = number + 1
        create_data_file(increment)
    finally:
        pass


create_data_file(0)


# exit script with CTRL-D when laundry program is finished
start_wumblering(laundry_id)
