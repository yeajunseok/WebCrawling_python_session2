import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위에 4줄 한이유는 Atom에서 한글을 출력하지 못하기 떄문에 문제 해결하기 위해 설정한다.

from bs4 import BeautifulSoup
html = """
<html><body>
  <ul>
    <li><a id="naver" href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="http://www.daum.com">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser')
print(soup.find(id = "naver").string) #id값으로 바로 찾기.

#정규 표현식으로 내가 원하는 값만 딱 뽑아준다. 앞과의 차이는 내가 조건을 걸수 있다.
#find, find_all에서 id,href같은 속성값으로 원하는 값을 뽑아낸다.
import re
li = soup.find_all(href=re.compile(r"^https://"))
print(li)
        #결과값: [<a href="https://www.google.com">google</a>, <a href="https://www.tistory.com">tistory</a>]
for e in li:
    print(e.attrs['href'])
        #결과값: https://www.google.com
        #결과값: https://www.tistory.com
li = soup.find_all(href=re.compile(r"da"))
for e in li:
    print(e.attrs['href'])
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
