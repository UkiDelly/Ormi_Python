import re
import requests
from bs4 import BeautifulSoup


class DailyTradingVolume:
    def __init__(
        self,
        날짜: str,
        *data: str,  # 종가: str, 전일비: str, 시가: str, 고가: str, 저가: str, 거래량: str
    ) -> None:
        self.날짜 = 날짜
        self.종가 = int(data[0].replace(",", ""))
        self.전일비 = int(data[1])
        self.시가 = int(data[2].replace(",", ""))
        self.고가 = int(data[3].replace(",", ""))
        self.저가 = int(data[4].replace(",", ""))
        self.거래량 = int(data[5].replace(",", ""))

    def __str__(self):
        return f"DailyTradingVolume(날짜: {self.날짜}, 종가: {self.종가}, 전일비: {self.전일비}, 시가: {self.시가}, 고가: {self.고가}, 저가: {self.저가}, 거래량: {self.거래량})"

    def __repr__(self) -> str:
        return f"DailyTradingVolume(날짜: {self.날짜}, 종가: {self.종가}, 전일비: {self.전일비}, 시가: {self.시가}, 고가: {self.고가}, 저가: {self.저가}, 거래량: {self.거래량})"


html = requests.get("https://www.paullab.co.kr/stock.html")
html.encoding = "utf-8"
soup = BeautifulSoup(html.text, "html.parser")


study = soup.select(" .main:nth-child(3)")[0]
rows = study.select("tbody > tr")
data: list[DailyTradingVolume] = []

for row in rows[1:]:
    date = row.select(" .date")
    spans = row.select(" .num > span")
    prices = [span.text for span in spans]
    new_vol = DailyTradingVolume(date[0].text, *prices)
    data.append(new_vol)


pattern = re.compile(r"2019[\.]10")
data = [x for x in data if pattern.match(x.날짜)]
answer = 0

for i in data:
    answer += i.거래량

print(f"10월 총 거래량은: {answer:,d}원입니다.")
