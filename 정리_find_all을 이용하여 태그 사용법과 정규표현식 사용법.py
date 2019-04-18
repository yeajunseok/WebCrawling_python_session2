import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위에 4줄 한이유는 Atom에서 한글을 출력하지 못하기 떄문에 문제 해결하기 위해 설정한다.

html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

##find() 사용법##
links_0 = soup.find("a") #첫번째 a태그만 담는다.
print('find 타입: ', type(links_0))
    #결과: <class 'bs4.element.Tag'>
print(links_0)
    #결과: <a href="http://www.naver.com">naver</a>
print(links_0.string)
    #결과: naver
print(links_0.attrs['href'])
    #결과: http://www.naver.com

##find_all() 사용법##
links_1 = soup.find_all("a") #a태그들을 모두 link변수에 담는다.
print('find_all 타입: ', type(links_1))
    #결과: <class 'bs4.element.ResultSet'>
print(links_1)
    #결과 > [<a href="http://www.naver.com">naver</a>, <a href="http://www.daum.net">daum</a>, <a href="https://www.google.com">google</a>, <a href="https://www.tistory.com">tistory</a>]

for a in links_1:
    print(type(a), a)
    print(a.string)
    print(a.attrs['href'])
#결과: <class 'bs4.element.Tag'> <a href="http://www.naver.com">naver</a>
#      naver
#      http://www.naver.com

#결과: <class 'bs4.element.Tag'> <a href="http://www.daum.net">daum</a>
#      daum
#      http://www.daum.net

#결과: <class 'bs4.element.Tag'> <a href="https://www.google.com">google</a>
#      google
#      https://www.google.com

#결과: <class 'bs4.element.Tag'> <a href="https://www.tistory.com">tistory</a>
#      tistory
#      https://www.tistory.com
links_2 = soup.find_all("a", string="daum")
print(links_2)
    #결과 > [<a href="http://www.daum.net">daum</a>]
links_3 = soup.find_all("a", limit=3) #3개만 갖고온다.
print(links_3)
    #결과 > [<a href="http://www.naver.com">naver</a>, <a href="http://www.daum.net">daum</a>, <a href="https://www.google.com">google</a>]
links_4 = soup.find_all(string=["naver","google"])
print(links_4)
    #결과 > ['naver', 'google']
'''
print(type(links_1))
#결과: <class 'bs4.element.ResultSet'>
#알수 있는점: find_all의 타입은 ResultSet이다!!
'''

##find_all에서 정규표현식 사용법##
import re
li_1 = soup.find_all(href=re.compile(r"^https://"))
print(li_1)
    #결과값: [<a href="https://www.google.com">google</a>, <a href="https://www.tistory.com">tistory</a>]
for e in li_1:
    print(e.attrs['href'])
    #결과값: https://www.google.com
    #결과값: https://www.tistory.com

li_2 = soup.find_all(href=re.compile(r"da"))
for e in li_2:
    print(e.ettrs['href'])
    #결과값: http://www.daum.net
    #결과값: http://www.daum.com
'''
soup.find_all(href=re.compile(r"^https://"))와
soup.find_all("a") 의 차이점

links_1 = soup.find_all("a") #a태그를 변수에 한방에 전부 담는다.
print(links_1)
    #결과값: [<a href="http://www.naver.com">naver</a>, <a href="http://www.daum.net">daum</a>, <a href="https://www.google.com">google</a>, <a href="https://www.tistory.com">tistory</a>]

li = soup.find_all(href=re.compile(r"^https://")) #정규표현식에 맞는 값만 담는다.
print(li)
    #결과값: [<a href="https://www.google.com">google</a>, <a href="https://www.tistory.com">tistory</a>]

!!!그러나 CSS선택자를 거의 많이 사용한다. 그냥 여기선 정규표현식으로도 뽑을수 있구나 정도만 알고 가자
'''
