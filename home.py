import json
import time
from flask import Flask, render_template

def home():
    title = 'Home'
    datadic = {}
    now = time.time()
    dstring = '/static/images/'
    qstring = '?' + str(time.time())
    piclist = [dstring + 'Light.jpeg'+qstring,
               dstring + 'Hum.jpeg'+qstring,
               dstring + 'Temps.jpeg'+qstring]
    with open("datadic.txt") as f:
        for line in f:
           (key, val) = line.split()
           datadic[key] = val
    return render_template('maindisplay.html', title=title, datadic=datadic, piclist=piclist)
