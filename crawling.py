import requests
from bs4 import BeautifulSoup
import pandas as pd

a = []
for i in range(14,30):
    response = requests.get(f"http://www.pigtimes.co.kr/news/articleView.html?idxno=458{i}")
    html = response.text
    if ("관리자가 검토중인 기사 입니다" in html) :
        break
    else :
        soup = BeautifulSoup(html, 'html.parser')

        links3 = soup.select(".updated")
        for link3 in links3:
            time = link3.text

        links =  soup.select(".article-head-title")
        for link in links:
            title = link.text

        links2 = soup.select("#article-view-content-div")
        for link2 in links2:
            article = link2.text
        
        a.append([time,title,article])
    
df = pd.DataFrame(a, columns=['time','title', 'article'])
df.to_csv('news.csv', index=False,encoding='utf8') 


    