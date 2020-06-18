from datetime import datetime
import statistics

from flask import Flask, render_template

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

def bokehtest(path):
    # prepare some data
    x = []
    y = []
    with open(path, 'r') as f:
        for line in f:
            data = line.split()
            time = datetime.strptime(data[0], '%H:%M:%S')
            x.append(time)
            y.append(float(data[4]))
    
    av = statistics.mean(y)
    p = figure(title="Fish Tank pH", x_axis_label='Time', y_axis_label='pH',
               x_axis_type='datetime')

    p.circle(x, y, size=5)
    p.line(x, av, legend_label="Average today: %f" % av, line_color="red") 
    
    script, div = components(p)
    
    return render_template("bokehtest.html", script=script, div=div)
