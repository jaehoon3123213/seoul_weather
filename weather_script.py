import requests
import csv
from datetime import datetime
import os
CITY ="Seoul"
API_KEY=os.getenv("OPENWEATHER_API_KEY")
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

data =requests.get(url).json()

temp = data["main"]["temp"]
humidity =data["main"]["humidity"]
weather = data["weather"][0]["description"]
time_zone = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

csv_filename = "seoul_weather.csv"
header =["timezone","temp","humidity","weather"]

file_exist = os.path.isfile(csv_filename)

#mode a - if not file - create
#if is file - write
with open(csv_filename,"a") as file:
    writer = csv.writer(file)
    if not file_exist:
         writer.writerow(header)
    writer.writerow([time_zone,temp,humidity,weather])
    print("csv저장완료")
