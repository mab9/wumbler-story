#!/usr/bin/env python3
import numpy as np
import pandas as pd
from numpy import ma
import matplotlib.pyplot as plt

## reduces the amount of data points. divide by 10
def reduce(data):
    return data[1:-1:10]

def denormalize_2G(filename):
    file = open("2018-12-03-xxx.wd", "a")
    df = pd.read_csv("2018-10-16-0.wd")
    for row in df.iterrows():
        x = int(round(16384*row[1][0]))
        y = int(round(16384*row[1][1]))
        z = int(round(16384*row[1][2]))
        r = str(x) + "," + str(y) + "," + str(z) + "\n"
        file.write(r)
    file.close()
    return

    
def transform_to_vector(panda):
    x = np.power(panda,2)
    s = np.sum(x, axis=1)
    return np.sqrt(s)


def plot_raw(df):
    fig = plt.figure()
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 4))

    _ = ax.scatter(df.index.values, df['x'].values, label='x',alpha=0.5)
    _ = ax.scatter(df.index.values, df['y'].values, label='y',alpha=0.5)
    _ = ax.scatter(df.index.values, df['z'].values, label='z',alpha=0.5)
    _ = ax.legend()

    _ = ax.set_ylabel('acceleration')
    _ = ax.set_xlabel('time')


#https://matplotlib.org/gallery/lines_bars_and_markers/step_demo.html#sphx-glr-gallery-lines-bars-and-markers-step-demo-py
def plot_masked(df):
    value = reduce(transform_to_vector(df))
    upper = np.mean(value) + 1*np.std(value)
    lower = np.mean(value) - 1*np.std(value)

    plt.step(np.arange(np.size(value)), value)

    label_m =  'mean: ' + str(np.mean(value))
    label_upper = 'mean + std: ' + str(upper) 
    label_lower = 'mean - std: ' + str(lower) 
    plt.axhline(np.mean(value), color='orange', label=label_m)
    plt.axhline(upper, color='red', label=label_upper)
    plt.axhline(lower, color='green', label=label_lower)
    
    m_value = ma.masked_where((value > lower ) & (value < upper), value)
    plt.step(np.arange(np.size(m_value)), m_value, label='masked values that are above / under std.')
    
    plt.legend()
    plt.xlabel('time')
    plt.ylabel('acceleration')
    plt.show()   
    
    
def plot_vector(df):  
    result = reduce(transform_to_vector(df))
    plt.step(np.arange(np.size(result)), result)
    plt.xlabel('time')
    plt.ylabel('acceleration')
  
    print("max: ", np.max(result))
    print("min: ", np.min(result))
    print("median: ", np.median(result))
    print("average: ", np.mean(result))
    print("std: ", np.std(result)) 
  