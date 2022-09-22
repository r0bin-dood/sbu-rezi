#!/bin/sh

echo "--------------------"
echo "Installing python3.7"
echo "--------------------"
sudo apt-get install -y python3.7 python3.7-venv

echo "--------------------------------"
echo "Installing and running mosquitto"
echo "--------------------------------"
sudo apt-get install -y mosquitto mosquitto-clients
if pgrep -x "mosquitto" >/dev/null
then
    echo "mosquitto already installed and running :D"
else
    mosquitto -c /etc/mosquitto/mosquitto.conf &
fi

echo "---------------------------"
echo "Installing ffmpeg and libav"
echo "---------------------------"
sudo apt-get install -y libav-tools libavcodec-extra ffmpeg

echo "------------------------------"
echo "Setting up virtual environment"
echo "------------------------------"
python3.7 -m pip install virtualenv
python3.7 -m venv ./sbu-rezi-env
source sbu-rezi-env/bin/activate

echo "------------------"
echo "Installing modules"
echo "------------------"
pip install --upgrade pip
pip install -r requirements.txt
pip install -r yolov5/requirements.txt

echo "--------------------"
echo "Done! HAPPY HACKING!"
echo "--------------------"