# PLEASE DO NOT SHARE *YOUR* TWILIO CREDS WITH ANYONE

import os
import argparse
import paho.mqtt.client as mqtt
from twilio.rest import Client 
from datetime import datetime
from threading import Thread
import time

parser = argparse.ArgumentParser(description='Start Rezi SMS Notification Server')
parser.add_argument('--i', type=str, default="localhost", help='IP address of server in the form 0.0.0.0, localhost if own computer')
parser.add_argument('--p', type=int, default=1883, help='MQTT port number (default 1883)')
parser.add_argument('--n', type=str, help='US phone number to send notifications to in the form 2015551234')
parser.add_argument('--s', type=int, default=30, help='Notification throttle')
parser.add_argument('--account_sid', type=str, default=os.environ.get('TWILIO_ACCOUNT_SID'), help='Please set environment variable TWILIO_ACCOUNT_SID')
parser.add_argument('--auth_token', type=str, default=os.environ.get('TWILIO_AUTH_TOKEN'), help='Please set environment variable TWILIO_AUTH_TOKEN')
parser.add_argument('--service_sid', type=str, default=os.environ.get('TWILIO_SERVICE_SID'), help='Please set environment variable TWILIO_SERVICE_SID')
args = parser.parse_args()

if not args.account_sid or not args.auth_token or not args.service_sid or not args.n:
    exit(parser.print_help())

client = Client(args.account_sid, args.auth_token) 

eventTopic = "@/detection"

global soundThread
soundThread = True

def on_message(mqttc, obj, msg):
    global soundThread
    if soundThread is True:
        soundThread = False
        thr = Thread(target=send_notificaiton, args=(msg,))
        thr.start()

    
def send_notificaiton(msg):
    global soundThread
    message = str(msg.payload.decode("utf-8"))

    print("{date} - Sending notification\n{message}\n".format(date=datetime.now(), message=message))

    message = client.messages.create(  
                      messaging_service_sid=args.service_sid, 
                      body=message,
                      to='+1' + args.n 
                  )
    print("Throttling for " + str(args.s) + " seconds")
    time.sleep(args.s)
    print("Ready...")
    soundThread = True

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.connect(args.i, args.p, 60)
mqttc.subscribe(eventTopic, 0)

print("Rezi SMS Notification Server")
print("Subscribed to " + eventTopic + " at " + args.i + ":" + str(args.p))
print("Sending notifications to +1" + args.n)
print("----------------------------------------")

mqttc.loop_forever()