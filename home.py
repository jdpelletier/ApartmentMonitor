import json
from flask import Flask, render_template

def home():
    title = 'Home'
    datadic = {}
    with open("datadic.txt") as f:
        for line in f:
           (key, val) = line.split()
           datadic[key] = val
    return render_template('maindisplay.html', title=title, datadic=datadic)
