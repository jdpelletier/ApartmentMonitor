from flask import Flask
from home import home

app = Flask(__name__)

# Establish etcgui route

@app.route('/')
def home_():
    return home()

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 50009
    app.run(host=host,port=port)