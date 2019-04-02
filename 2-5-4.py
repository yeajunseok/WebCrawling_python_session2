'''
2-5-1에선 직접접근이로...
2-5-3에선 tag 선택자로 직접접근하여 사용한다.
2-5-4에선 CSS 선택자를 이용해서 조건에 맞는 엘리먼트를 찾아~~ 스크래핑에서 가장 많이 사용된다. <정확한 타켓을 한번에 딱!!!>
'''
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위에 4줄 한이유는 Atom에서 한글을 출력하지 못하기 떄문에 문제 해결하기 위해 설정한다.

from bs4 import BeautifulSoup
html = """
<html><body>
<div id="main">
  <h1>강의목록</h1>
  <ul class="lecs">
    <li>Java 초고수 되기</li>
    <li>파이썬 기초 프로그래밍</li>
    <li>파이썬 머신러닝 프로그래밍</li>
    <li>안드로이드 블루투스 프로그래밍</li>
  </ul>
</div>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser')

###soup.select()###
h1 = soup.select("div#main > h1") #div 태그에서 id=main인것 중에 하위에 h1인 태그
print('h1', h1) #print('h1', type(h1))
print('h1', type(h1)) #<class 'list'>, 리스트 타입이다. 그래서...
print('h1', h1[0].string)
#또는
for z in h1:
    print(z.string)

###soup.select_one###
h1_1 = soup.select_one("div#main > h1")
print("h1_1:", h1_1) #<h1>강의목록</h1>
print('h1_1:', h1_1.string) #강의목록
'''
둘의 차이점은
가지고 올때 딱 하나면 select_one을 사용하고, 그게 아니면 select사용한다.
'''

list_li = soup.select("div#main > ul.lecs > li")
for li in list_li:
    print("li:", li.string)
            #li: Java 초고수 되기
            #li: 파이썬 기초 프로그래밍
            #li: 파이썬 머신러닝 프로그래밍
            #li: 안드로이드 블루투스 프로그래밍
