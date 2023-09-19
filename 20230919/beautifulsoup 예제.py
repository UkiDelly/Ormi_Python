import requests
from bs4 import BeautifulSoup

paullab_url = "http://paullab.co.kr/bookservice/"
response = requests.get(paullab_url)
response.encoding = "utf-8"
html = response.text

soup = BeautifulSoup(html, "html.parser")

bookservices = soup.select(".col-lg-6 > h2")  # col-lg-6 클래스 안의 h2 태그 탐색
for no, book in enumerate(bookservices, 1):
    print(no, book.text)
