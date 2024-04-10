#!/usr/bin/env python3

from flask import Flask, jsonify
import speedtest

app = Flask(__name__)

@app.route('/')
def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download(threads=None) / 1000000  # Mbps
    download_speed = round(download_speed, 2)
    if download_speed <= 50:
        text = f"󰾆 {download_speed}"

    elif download_speed > 50 and download_speed <= 100:
        text = f"󰾅 {download_speed}"

    elif download_speed > 100:
        text = f"󰓅 {download_speed}"

    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True, port=1530)
