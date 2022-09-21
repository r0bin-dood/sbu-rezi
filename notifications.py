"""
Steps:
1. Install paho-mqtt and twilio if not already installed
    a. python3 -m pip install paho-mqtt
    b. python3 -m pip install twilio
2. If on VPN, disconnect
2. PLEASE DO NOT SHARE *YOUR* TOKENS WITH ANYONE
"""
import os
import argparse
import paho.mqtt.client as mqtt
from twilio.rest import Client 
import json
import subprocess
import sys
from datetime import datetime
import requests

parser = argparse.ArgumentParser(description='Start Rezi SMS Notification Server')
parser.add_argument('--i', type=str, default="localhost", help='IP address of server in the form 0.0.0.0, localhost if own computer')
parser.add_argument('--p', type=int, default=1883, help='MQTT port number (default 1883)')
parser.add_argument('--n', type=str, help='US phone number to send notifications to in the form 2015551234')
parser.add_argument('--s', type=int, default=30, help='Notification throttle')
parser.add_argument('--account_sid', type=str, default=os.environ.get('TWILIO_ACCOUNT_SID'), help='Please set environment variable TWILIO_ACCOUNT_SID')
parser.add_argument('--auth_token', type=str, default=os.environ.get('TWILIO_AUTH_TOKEN'), help='Please set environment variable TWILIO_AUTH_TOKEN')
parser.add_argument('--service_sid', type=str, default=os.environ.get('TWILIO_SERVICE_SID'), help='Please set environment variable TWILIO_SERVICE_SID')
args = parser.parse_args()

if not args.account_sid or not args.auth_token or not args.service_sid:
    exit(parser.print_help())

client = Client(args.account_sid, args.auth_token) 

eventTopic = "@/detection"

bodyTemplate = '\
\n{event} event from {devId} triggered a clip capture.\n\n\
Clip: {clip}\
'
def on_message(mqttc, obj, msg):
    message = str(msg.payload.decode("utf-8"))
    parsedMessage = json.loads(message)

    print("{date} - Sending notification\n{message}\n\n".format(date=datetime.now(), message=parsedMessage))

    message = client.messages.create(  
                      messaging_service_sid=args.service_sid, 
                      body=parsedMessage,
                      to='+1' + args.n 
                  )

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.connect(args.i, args.p, 60)
mqttc.subscribe(eventTopic, 0)

print("Rezi SMS Notification Server")
print("Subscribed to " + eventTopic + " at " + args.i + ":" + str(args.p))
print("Sending notifications to +1" + args.n)
print("----------------------------------------")

mqttc.loop_forever()