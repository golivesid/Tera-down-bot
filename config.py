import os

#Database 
#Database [https://youtu.be/qFB0cFqiyOM?si=fVicsCcRSmpuja1A]
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://tony:tera@tera.kr6muwi.mongodb.net/?retryWrites=true&w=majority&appName=tera")
DB_NAME = os.environ.get("DATABASE_NAME", "tera")

#Shortner (token system) 
# check my discription to help by using my refer link of shareus.io


SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "ziplinker.net")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "4b884da539a2f5d579e2a6f805e623c7a082a3b1")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 43200)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "false")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/ultroid_official/18") # shareus ka tut_vid he 
