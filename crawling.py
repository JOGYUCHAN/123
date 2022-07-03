import requests
from bs4 import BeautifulSoup
import pandas as pd

a = []
for i in range(600,800):
    response = requests.get(f"http://www.pigtimes.co.kr/news/articleView.html?idxno=45{i}")
    url = f"http://www.pigtimes.co.kr/news/articleView.html?idxno=45{i}"
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    if("관리자가 검토중인 기사 입니다." in html) or("존재하지 않는 링크" in html):
        continue
    else:
        name = soup.select_one(".article-head-nav>a").get_text()
        theme = name
        links3 = soup.select(".updated")
        for link3 in links3:
            time = link3.text

        links =  soup.select(".article-head-title")
        for link in links:
            title = link.text

        links2 = soup.select("#article-view-content-div")
        for link2 in links2:
            arti = link2.text
            article = arti.replace("\n","").replace(" 저작권자 © 양돈타임스 무단전재 및 재배포 금지김현구다른기사 보기 ","")

    a.append([time, theme , title, article])

df = pd.DataFrame(a,columns=['time','theme','title','article'])
df.to_csv("news.csv",index=False, encoding='utf8')

    


    