import argparse
import paho.mqtt.client as mqtt
from pydub import AudioSegment
from pydub.playback import play
from threading import Thread
import time


parser = argparse.ArgumentParser(description='Start Rezi SMS Notification Server')
parser.add_argument('--i', type=str, default="localhost", help='IP address of server in the form 0.0.0.0, localhost if own computer')
parser.add_argument('--p', type=int, default=1883, help='MQTT port number (default 1883)')
parser.add_argument('--s', type=int, default=30, help='Alarm throttle')
parser.add_argument('--f', type=str, help='Audio file to play')
args = parser.parse_args()

if not args.f:
    exit(parser.print_help())

eventTopic = "@/detection"

global soundThread
soundThread = True

def on_message(mqttc, obj, msg):
    global soundThread
    if soundThread is True:
        soundThread = False
        thr = Thread(target=playSound)
        thr.start()

def playSound():
    global soundThread
    print("Playing sound")
    sound = AudioSegment.from_mp3(args.f)
    play(sound)
    print("Throttling for " + str(args.s) + " seconds")
    time.sleep(args.s - int(sound.duration_seconds))
    print("Ready to play...")
    soundThread = True

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.connect(args.i, args.p, 60)
mqttc.subscribe(eventTopic, 0)

print("Rezi Alarm Server")
print("Subscribed to " + eventTopic + " at " + args.i + ":" + str(args.p))
print("Playing sound " + args.f)
print("----------------------------------------")

mqttc.loop_forever()