import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위에 4줄 한이유는 Atom에서 한글을 출력하지 못하기 떄문에 문제 해결하기 위해 설정한다.

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
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

######CSS선택자를 이용한######
##select() 사용법##
se1_1 = soup.select("div#main > ul.lecs > li")
print(se1_1)        #결과: [<li>Java 초고수 되기</li>, <li>파이썬 기초 프로그래밍</li>, <li>파이썬 머신러닝 프로그래밍</li>, <li>안드로이드 블루투스 프로그래밍</li>]
for s in se1_1:
    print(s.string) #결과: Java 초고수 되기 / 파이썬 기초 프로그래밍 / 파이썬 머신러닝 프로그래밍 / 안드로이드 블루투스 프로그래밍

se1 = soup.select("div#main > h1")
print(type(se1))     #결과: <class 'list'>
print(se1)           #결과: [<h1>강의목록</h1>]
print(se1[0].string) #결과: 강의목록
for z in se1:
    print(z.string)
                    #결과: 강의목록

##select_one() 사용법##
se2 = soup.select_one("div#main > h1")
print(type(se2))    #결과: <class 'bs4.element.Tag'>
print(se2)          #결과: <h1>강의목록</h1>
print(se2.string)   #결과: 강의목록

##select와 select_one의 차이점##
#가지고 올때 딱 하나면 select_one을 사용하고, 그게 아니면 select사용한다.
#select_one은 tag 타입이고, select는 list타입니다.

######정규식을 이용한######
##select_one과 select##
print(soup.select_one("li:nth-of-type(1)").string)              #결과: 닭도리탕
print(soup.select_one("#ac-list > li:nth-of-type(4)").string)   #결과: 양주
print(soup.select("#ac-list > li[data-lo='cn']")[0].string)     #결과: 양주, select는 list형태로 반환한다.
print(soup.select("#ac-list > li.alcohol.high")[0].string)      #결과: 양주
print(soup.select("#ac-list > li[class='alcohol']")[1].string)  #결과: 맥주, select는 list형태로 반환한다.

##find와 find_all##
param = {"data-lo":"cn", "class":"alcohol"}
print(soup.find("li",param).string)                             #결과: 양주
print(soup.find(id="ac-list").find("li",param).string)          #결과:양주

for ac in soup.find_all("li"):
    if ac['data-lo'] == 'us':
        print('data-lo == us', ac.string)
                                                                #결과: data-lo == us 스테이크
                                                                #     data-lo == us 맥주

'''
select와 find의 차이점
https://stackoverflow.com/questions/38028384/beautifulsoup-is-there-a-difference-between-find-and-select-python-3-x
select finds multiple instances and returns a list, find finds the first, so they don't do the same thing. select_one would be the equivalent to find.
I almost always use css selectors when chaining tags or using tag.classname, if looking for a single element without a class I use find. Essentially it comes down to the use case and personal preference.
'''
