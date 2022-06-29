import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("http://www.pigtimes.co.kr/news/articleView.html?idxno=45814")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

links2 = soup.select("#article-view-content-div")
for link2 in links2:
    article = link2.text

print(article)