import datetime
import requests
import time as delay
from pygame import mixer, time

# load azan.mp3
mixer.init()
mixer.music.load('C:/Users/HP/Downloads/RasPi_Ramadhan_INDONESIA/azan.mp3')

# request aladhan api
url = 'http://api.aladhan.com/v1/timingsByCity?city=Jakarta&country=Indonesia&method=5'
data = requests.get(url)
output = data.json()
output = output['data']['timings']

imsak = output['Imsak']
subuh = output['Fajr']
duhur = output['Dhuhr']
asar = output['Asr']
magrib = output['Maghrib']
isya = output['Isha']
print(imsak, subuh, duhur, asar, magrib, isya)

while True:
    # time now
    x = datetime.datetime.now()
    jam = x.strftime("%H") # jam sistem 24
    menit = x.strftime("%M") # menit
    detik = x.strftime("%S") # detik
    
    print(f'{jam}:{menit}:{detik}')
    if jam == str(a) and menit == str(b):
        print('Waktunya azan')
        mixer.music.play()
        while mixer.music.get_busy(): 
            time.Clock().tick(10)
    
    delay.sleep(1) # delay 1s