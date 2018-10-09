#!/usr/bin/env python3$

import math
import time

import sensor


def calibrate(laundryId, duration):
    if duration is None:
        duration = 5

    print("start calibration for:", duration, "seconds")
    timeout = time.time() + duration

    x = []
    y = []
    z = []

    while True:
        if time.time() > timeout:
            break

        data = sensor.readAcc()
        x.append(data[0])
        y.append(data[1])
        z.append(data[2])
        time.sleep(0.1)

    return prepareData(laundryId, x, y, z)


def calcAvg(data):
    sum = 0
    for x in data:
        sum += x
    return int(sum / len(data))


def calcStandardDeviation(lst):
    num_items = len(lst)
    mean = sum(lst) / num_items
    differences = [x - mean for x in lst]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
    variance = ssd / (num_items - 1)
    return int(math.sqrt(variance))


def prepareData(laundryId, x, y, z):
    data = []
    data.append(laundryId)
    data.append(len(x))
    data.append(calcAvg(x))
    data.append(calcStandardDeviation(x))
    data.append(calcAvg(y))
    data.append(calcStandardDeviation(y))
    data.append(calcAvg(z))
    data.append(calcStandardDeviation(z))
    data.append("&")
    return data
