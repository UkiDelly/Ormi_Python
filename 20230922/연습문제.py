# 문제1 https://www.paullab.co.kr/stock.html 서비스를 크롤링하여 제주코딩베이스캠프 연구원의 2019년 10월 총 거래량을 구해주세요.

# 문제2 html에서 태그를 제거하고 텍스트만 뽑아낼 수 있도록 해주세요.
# '<p>This is a <em>simple</em> example.</p>'

# 문제3 아래 텍스트에서 이메일만 추출할 수 있는 정규표현식을 만들어주세요.
# '제 이메일 주소는 example1@gmail.com이고 회사 이메일 주소는 example2@gmail.com 입니다.
# example1로 연락을 주셨다면 제게 메시지 한 번 부탁드립니다.'

import re
import requests
from bs4 import BeautifulSoup

# 문제 1번  https://www.paullab.co.kr/stock.html 서비스를 크롤링하여 제주코딩베이스캠프 연구원의 2019년 10월 총 거래량을 구해주세요.
html = requests.get("https://www.paullab.co.kr/stock.html")
html.encoding = "utf-8"
soup = BeautifulSoup(html.text, "html.parser")

study = soup.select(" .main:nth-child(3)")
table = study.select("tbody > tr")
data = []

for i in table[1:]:
    date = i.select(" .date")[-1].text
    price = i.select(" .num > span")[-1].text
    price = price.replace(",", "")
    data.append((date, int(price)))

date_pattern = re.compile(r"2019[\.]10")

result = sum(price for date, price in data if date_pattern.match(date))

print(f"10월 총 거래량은: {result:,d}원입니다,")


# 문제2 html에서 태그를 제거하고 텍스트만 뽑아낼 수 있도록 해주세요.
# '<p>This is a <em>simple</em> example.</p>'
string = "<p>This is a <em>simple</em> example.</p>"
html_tag_pattern = re.compile(r"(<[\w]+> | </[\w]+>)")
text = re.sub(r"<[\/]?[\w]+>", "", string)
print(text)

# # 문제3 아래 텍스트에서 이메일만 추출할 수 있는 정규표현식을 만들어주세요.
# # '제 이메일 주소는 example1@gmail.com이고 회사 이메일 주소는 example2@gmail.com 입니다.
# # example1로 연락을 주셨다면 제게 메시지 한 번 부탁드립니다.'
email_string = "제 이메일 주소는 example1@gmail.com이고 회사 이메일 주소는 example2@gmail.com 입니다.example1로 연락을 주셨다면 제게 메시지 한 번 부탁드립니다."
email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
emails = email_pattern.findall(email_string)
print(emails)
