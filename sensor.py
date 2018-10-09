#!/usr/bin/env python3

import time

import smbus

# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

# accolemeter config
ACCEL_2G = 0x00
ACCEL_4G = 0x08
ACCEL_8G = 0x10
ACCEL_16G = 0x18

# Scale Modifiers
ACCEL_SCALE_MODIFIER_2G = 16384.0
ACCEL_SCALE_MODIFIER_4G = 8192.0
ACCEL_SCALE_MODIFIER_8G = 4096.0
ACCEL_SCALE_MODIFIER_16G = 2048.0


def read_byte(reg):
    return bus.read_byte_data(address, reg)


def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg + 1)
    value = (h << 8) + l
    return value


def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val


bus = smbus.SMBus(1)
address = 0x68

# Aktivieren, um das Modul ansprechen zu koennen

bus.write_byte_data(address, power_mgmt_1, 0)
bus.write_byte_data(address, power_mgmt_1, ACCEL_2G)

minute = 1
seconds = 60
timeout = time.time() + seconds * minute


# filename = time.strftime("%Y%m%d-%H:%M")
def readAcc():
    data = []
    data.append(abs(read_word_2c(0x3b)))
    data.append(abs(read_word_2c(0x3d)))
    data.append(abs(read_word_2c(0x3f)))
    return data
