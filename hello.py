from flask import Flask
import os
import metrics_tracker_client

app = Flask(__name__)
metrics_tracker_client.track() # Trackingするなら必要

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
port = os.getenv('PORT', '5000') # portはIBM Cloud環境から割り当てられたものを利用

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port), debug=True) # Procfile内でpython hello.pyで起動