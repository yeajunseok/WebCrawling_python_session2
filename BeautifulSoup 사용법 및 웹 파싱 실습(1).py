'''
1. 다음 금융 시가총액 상위종목 가져오기
2. 네이버 금융 TOP 10종목 가져오기
3. 인프런 추천 강좌 10개 가져오기
'''
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위에 4줄 한이유는 Atom에서 한글을 출력하지 못하기 떄문에 문제 해결하기 위해 설정한다.

from bs4 import BeautifulSoup
import urllib.request as req

url = "http://finance.daum.net/domestic/market_cap?market=KOSPI"
req = req.urlopen(url).read()
soup = BeautifulSoup(req, "html.parser")

#print('soup', soup.prettify())
top = soup.select("ul#myListTop1 > li")

for i,e in enumerate(top,1):
    print(i,e.find("a").string, "=", e.find("span").string)
