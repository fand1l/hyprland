#!/usr/bin/env python3

from flask import Flask, jsonify
import speedtest
import distro
import psutil

app = Flask(__name__)

@app.route('/get_internet_speed')
def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download(threads=None) / 1000000  # Mbps
    download_speed = round(download_speed, 2)
    if download_speed <= 50:
        netspeed = f"󰾆 {download_speed}"

    elif download_speed > 50 and download_speed <= 100:
        netspeed = f"󰾅 {download_speed}"

    elif download_speed > 100:
        netspeed = f"󰓅 {download_speed}"

    return jsonify({'text': netspeed})


@app.route('/get_distro_icon')
def get_distro_icon():
    distro_id = distro.id()

    if distro_id == "arch":
        distro_icon = "󰣇"

    elif distro_id == "debian":
        distro_icon = ""

    elif distro_id == "ubuntu":
        distro_icon = ""

    elif distro_id == "artix":
        distro_icon = ""

    elif distro_id == "opensuse":
        distro_icon = ""

    elif distro_id == "suse":
        distro_icon = ""

    elif distro_id == "centos":
        distro_icon = ""

    elif distro_id == "fedora":
        distro_icon = ""

    elif distro_id == "redhat":
        distro_icon = ""

    elif distro_id == "nixos" or distro_id == "nix":
        distro_icon = "󱄅"

    elif distro_id == "gentoo":
        distro_icon = "󰣨"

    elif distro_id == "void":
        distro_icon = ""

    elif distro_id == "manjaro":
        distro_icon = "󱘊"

    return jsonify({'text': distro_icon})
    

if __name__ == '__main__':
    app.run(debug=True, port=1530)
