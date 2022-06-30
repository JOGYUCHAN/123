import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("http://www.pigtimes.co.kr/news/articleView.html?idxno=45813")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links2 = soup.select_one(".article-head-nav>a").get_text()
# links2 = soup.find("a",{"href" : "/news/articleList.html?sc_section_code=S1N14"}).find_all(text = True)
# print(links2)

print(links2)

# for link2 in links2:
#     article = link2.text

# a = article.replace("\n","").replace("저작권자 © 양돈타임스 무단전재 및 재배포 금지양돈타임스다른기사 보기","")
# a.rstrip("©")
# print(a)

# f = open("test.txt","w",encoding='utf8')
# f.write(a)