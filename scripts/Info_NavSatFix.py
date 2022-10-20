#!/usr/bin/env python
import rospy
from sensor_msgs.msg import NavSatFix
import pyrebase

config = {
  "apiKey": "AIzaSyB9RkZFAwtJfZUXYvXZBb2S4GYVSzOkpjEv",
  "authDomain": "location-a26be.firebaseapp.com",
  "databaseURL": "https://location-a26be-default-rtdb.asia-southeast1.firebasedatabase.app",
  "storageBucket": "location-a26be.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def callback(data):
    rospy.loginfo("Longitude: %f, Latitude %f" % (data.longitude, data.latitude))
    longitude = data.longitude
    latitude = data.latitude

    data = {
    "latitude": latitude,
    "longitude": longitude
    }
    try:
        results = db.child("locationCar").update(data)
    except Exception:
        print("Error SentData")
    #Call for the programName(longitude,latitude)

def infoGetter():

    rospy.init_node('info_ublox_gps', anonymous=True)

    rospy.Subscriber("/ublox_gps/fix", NavSatFix, callback)#First parameter is the name of the topic

    rospy.spin()

if __name__ == '__main__':
    infoGetter()