import json
import time
from flask import Flask, render_template

def fish():
    title = 'pH'
    datadic = {}
    now = time.time()
    dstring = '/static/images/'
    qstring = '?' + str(time.time())
    piclist = [dstring + 'pH.jpeg'+qstring]
    with open("datadic.txt") as f:
        for line in f:
           (key, val) = line.split()
           datadic[key] = val
    return render_template('fishtank.html', title=title, datadic=datadic, piclist=piclist)