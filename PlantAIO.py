import serial
import time
import datetime
import Util
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from flask import Flask, render_template


def plantAIO():
    # Read and record the data
    values = []
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    t = []
    currentDay = datetime.date.today()
    path = Util.FolderCreate(currentDay)
    startTime = datetime.datetime.now()
    while(True):
        if currentDay != datetime.date.today():
            currentDay = datetime.date.today()
            path = Util.FolderCreate(currentDay)
            startTime = datetime.datetime.now()
            data1 = []
            data2 = []
            data3 = []
            data4 = []
        ser = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(5)
        b = ser.readline()         # read a byte string
        try:
            string_n = b.decode()      # decode byte string into Unicode
        except UnicodeDecodeError:
            print("Decode Error")
            continue
        string = string_n.rstrip() # remove \n and \r
        values = string.split()
        if len(values) != 4:
            print("Read Error")
            continue
        values[0] = float(values[0])
        values[1] = float(values[1])
        values[2] = float(values[2])
        values[3] = float(values[3])
        data1.append(values[0])           # add to the end of data list
        data2.append(values[1])
        data3.append(values[2])
        data4.append(values[3])
        t = [startTime + datetime.timedelta(minutes=5*i) for i in range(len(data1))]
        plt.plot(t, data1, 'ro')
        xformatter = mdates.DateFormatter('%H:%M')
        plt.gcf().axes[0].xaxis.set_major_formatter(xformatter)
        plt.title('Light (lums)')
        plt.savefig("Light.jpeg")
        plt.close()
        plt.plot(t, data2, 'bs')
        plt.gcf().axes[0].xaxis.set_major_formatter(xformatter)
        plt.title('Humidity (%)')
        plt.savefig("Hum.jpeg")
        plt.close()
        plt.plot(t, data3, 'g^')
        xformatter = mdates.DateFormatter('%H:%M')
        plt.gcf().axes[0].xaxis.set_major_formatter(xformatter)
        plt.title('Temperature (f)')
        plt.savefig("Temps.jpeg")
        plt.close()
        plt.plot(t, data4, 'b^')
        xformatter = mdates.DateFormatter('%H:%M')
        plt.gcf().axes[0].xaxis.set_major_formatter(xformatter)
        plt.title('pH')
        plt.savefig("pH.jpeg")
        plt.close()
        Util.FileWrite(path, string)
        Util.HandlePlot(path, "Light.jpeg")
        Util.HandlePlot(path, "Hum.jpeg")
        Util.HandlePlot(path, "Temps.jpeg")
        Util.HandlePlot(path, "pH.jpeg")
        maxes = [np.amax(data1), np.amax(data2), np.amax(data3), np.amax(data4)]
        string = string + " " + str(maxes[0]) + " " + str(maxes[1]) + " " + str(maxes[2]) + " " + str(maxes[3])
        Util.HTMLDic(string)
        ser.close()
        time.sleep(295)            # wait 5 minutes
    return


if __name__=='__main__':
    plantAIO()