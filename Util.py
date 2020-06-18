import os
import datetime
import shutil

def NowString():
    today = datetime.datetime.now()
    time = today.time().strftime('%H:%M:%S ')
    return time

def FileWrite(filepath, data):
    filename = os.path.join(str(filepath), "dataFile.txt")
    with open(filename, 'a') as f:
        f.write(NowString())
        f.write(data)
        f.write("\n")
        f.close()


def FolderCreate(today):

    todaystr = today.isoformat()

    parent_directory = "/home/pi/Desktop/ApartmentMonitor/TestData"
    path = os.path.join(parent_directory, todaystr)
    try:
        os.mkdir(path)
    except OSError:
        print ("The folder %s is already created" % path)
    else:
        print ("Successfully created the directory %s " % path)
    return path


def HandlePlot(path, image):
    test_dir = path
    image_dir = "/home/pi/Desktop/ApartmentMonitor/static/images"
    shutil.copy(image, test_dir)
    shutil.copy(image, image_dir)
    os.remove(image)

def HTMLDic(data):
    currentDay = datetime.date.today()
    daystring = currentDay.isoformat()
    data = data.split()
    datadic = {'today': daystring,
                'maxlum': data[4],
                'maxhum': data[5],
                'maxtemp': data[6],
                'maxph': data[7],
                'now': NowString(),
                'lum': data[0],
                'hum': data[1],
                'temp': data[2],
                'ph':data[3]}
    with open('datadic.txt', 'w') as f:
        for key in datadic:
            print(key + ' ' + datadic[key], file=f)
