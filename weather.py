import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://www.weather.go.kr/w/obs-climate/land/city-obs.do?auto_man=m&stn=0&dtm=&type=t99&reg=100&tm=2022.07.01.10%3A00")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
list = ["구미","홍천","부여"]
a = []
for i in list:
    link = soup.find("a",string = f"{i}")
    link1 = link.parent
    place = link1.text
    link2 = link1
    for i in range(0,10):
        link2 = link2.next_sibling
    temp = link2.text
    link3 = link1
    for i in range(0,18):
        link3 = link3.next_sibling
    hum = link3.text

    a.append([place,temp,hum])

df = pd.DataFrame(a,columns=['place','temparature','humidity'])
df.to_csv("weather.csv",index=True,encoding='utf8')









