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
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</div>
</body></html>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

###soup.find()###
find = soup.find("a")       #첫번째 a태그만 담는다.
print(type(find))           #결과: <class 'bs4.element.Tag'>
print(find)                 #결과: <a href="http://www.naver.com">naver</a>
print(find.string)          #결과: naver
print(find.attrs['href'])   #결과: http://www.naver.com
###soup.select_one###
select_one1 = soup.select_one("div#main > ul.lecs > li")
print(type(select_one1))         #결과: <class 'bs4.element.Tag'>
print(select_one1)               #결과: <li><a href="http://www.naver.com">naver</a></li>
print(select_one1.string)        #결과: naver
#print(select_one1.attrs['href']) #결과: 오류!!!
select_one2 = soup.select_one("div#main > h1")
print(type(select_one2))         #결과: <class 'bs4.element.Tag'>
print(select_one2)               #결과: <h1>강의목록</h1>
print(select_one2.string)        #결과: 강의목록
#print(select_one2.attrs['href']) #결과: 오류!!!


###soup.find_all()###
find_all = soup.find_all("a")   #a태그들을 모두 link변수에 담는다.
print(type(find_all))           #결과: <class 'bs4.element.ResultSet'>
print(find_all)                 #결과: [<a href="http://www.naver.com">naver</a>, <a href="http://www.daum.net">daum</a>, <a href="https://www.google.com">google</a>, <a href="https://www.tistory.com">tistory</a>]
for f_a in find_all:
    print(f_a)                  #결과: <a href="http://www.naver.com">naver</a>
    print(f_a.string)           #결과: naver
    print(f_a.attrs['href'])    #결과: http://www.naver.com
###soup.select()###
select_1 = soup.select("div#main > ul.lecs > li")
print(type(select_1))           #결과: <class 'list'>
print(select_1)                 #결과: [<li><a href="http://www.naver.com">naver</a></li>, <li><a href="http://www.daum.net">daum</a></li>, <li><a href="https://www.google.com">google</a></li>, <li><a href="https://www.tistory.com">tistory</a></li>]
print(select_1[0].string)       #결과: naver
for s_1 in select_1:
    print(s_1.string)           #결과: naver / daum / google / tistory

select_2 = soup.select("div#main > h1")
