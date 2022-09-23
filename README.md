# sbu-rezi


If you want to take full advantage of this project you should read this 
document carefully, as it's going to help you understand how to leverage the 
tools and resources being provided.


# for training your own dataset steps go to "README_OD.md"


# goals


Our goal is to use YOLOv5 to perform object detection and introduce MQTT as an
 interprocess messaging system. The main attraction is the notification.py 
script that uses MQTT to receive events and communicate with the outside world 
through Twilio.


By using and studying the project you should be able to:
- Use YOLOv5 to do object detection
- Create your own MQTT clients using Paho
- Send SMS to US phone numbers from a Python script using Twilio
- Play sounds leveraging ALSA and libav through the pydub module


This project includes a clone of the YOLOv5 project on GitHub, found here 
https://github.com/ultralytics/yolov5, without any version control. If your 
intent is to work with YOLOv5 only and not leverage the Resideo notification 
system, your work should be contained to the yolov5/ directory, or, you could 
clone the YOLOv5 repository directly outside of thie project folder.


# requirements


This project was written and tested on a Debian based Linux system. Ubuntu 18 
or 20 should work fine. Raspbian is also probably fine though untested.


# installation & usage


Before running any of the scripts, make sure you run "setup.sh" first.
setup.sh installs the necessary libraries and utilities for this demo and 
YOLOv5 to run.


It will create a virtual environment so:
*** Remember to run "deactivate" when you're done with virtual environment ***


Please pay close attention to how the script is run, not "./setup.sh" but 
". setup.sh" instead. Running with "./setup.sh" will apply the changes in 
another shell, not your current shell, and you don't want that.


Start with:

$ . setup.sh


If you need to reset the project:

$ . resetenv.sh


When done with the virtual environment:

$ deactivate


If you already have called setup.sh and want to activate the virtual 
environment, you can run:

$ source sbu-rezi-env/bin/activate
