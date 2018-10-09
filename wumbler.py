#!/usr/bin/env python3

import time
import uuid

import requests

import calibrator
import sensor

laundryId = uuid.uuid4()
serverUrl = "http://192.168.1.103:8080/"
calibration = None


def startWumblering(laundryId):
    print("laundry with id: ", laundryId, " has started")
    while True:

        data = []
        data.append(laundryId)
        data.append("&")

        for _ in range(10):
            data.append(sensor.readAcc())
            data.append("&")
            time.sleep(0.1)

        pushData(data)


def pushData(data):
    try:
        response = requests.post(serverUrl + 'collector', data={'data': data})
        if response.status_code == 422:
            print('[!] [{0}] wumbler not calibrated, try to submit calibration: [{1}]'.format(response.status_code,
                                                                                              laundryId))
            global calibration
            pushCalibration(calibration)
    except requests.exceptions.RequestException as e:
        now = time.ctime(int(time.time()))
        print("could not send sensor data to the server (connection error). " + str(now))


def calibrateWumbler(laundryId):
    global calibration
    calibration = calibrator.calibrate(laundryId, 4)
    pushCalibration(calibration)


def pushCalibration(calibration):
    try:
        requests.post(serverUrl + 'collector/calibration', data={"data": calibration})
    except requests.exceptions.RequestException as e:
        now = time.ctime(int(time.time()))
        print("could not send calibration data to the server (connection error). " + str(now))


calibrateWumbler(laundryId)
startWumblering(laundryId)
