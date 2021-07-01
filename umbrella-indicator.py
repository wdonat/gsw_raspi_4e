import requests
import time
from gpiozero import LED

key = '<YOUR API KEY HERE>'
latitude = '<YOUR LATITUDE>'  # Use quotes to make it a string
longitude = '<YOUR LONGITUDE>'  # Again, use quotes
api_url = 'https://api.weather.com/v3/wx/forecast/daily/5day?geocode=' + latitude + ',' + longitude + '&format=json&units=e&language=en-US&apiKey=' + key

while True:
    r = requests.get(api_url)
    forecast = r.json()
    pop_value = forecast['daypart'][0]['precipChance']
    if pop_value is None:
        pop_value = 0
    if pop_value >= 30: 
        led.on()
    else:
        led.off()
    time.sleep(180) # 3 minutes