import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import timedelta,date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


start_date = date(2018, 1, 1)
end_date = date(2018, 2, 1)
a = []
for sigle_date in daterange(start_date, end_date):
    print (sigle_date.strftime('%Y.%m.%d'))
    response = requests.get(f"https://www.weather.go.kr/w/obs-climate/land/city-obs.do?auto_man=m&stn=0&dtm=&type=t99&reg=100&tm={sigle_date.strftime('%Y.%m.%d')}.10%3A00")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    list = ["구미","홍천","부여","서울"]
    time = sigle_date.strftime('%Y.%m.%d')
    for str in list:
        link = soup.find("a",string = f"{str}")
        link1 = link.parent
        place = str
        link2 = link1
        for i in range(0,10):
            link2 = link2.next_sibling
        temp = link2.text
        link3 = link1
        if (sigle_date.month > 4) and (sigle_date.month < 10):
            for i in range(0,18):
                link3 = link3.next_sibling
                hum = link3.text
        else :
            for i in range(0,20):
                link3 = link3.next_sibling
                hum = link3.text


        a.append([time,place,temp,hum])

df = pd.DataFrame(a,columns=['time','place','temparature','humidity'])
df.to_csv("weather.csv",index=False,encoding='utf8')









