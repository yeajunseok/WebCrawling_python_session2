'''
2-5-1에선 직접접근이로...
2-5-3에선 tag 선택자로 직접접근하여 사용한다.
'''
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위에 4줄 한이유는 Atom에서 한글을 출력하지 못하기 떄문에 문제 해결하기 위해 설정한다.

from bs4 import BeautifulSoup
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

soup = BeautifulSoup(html, 'html.parser')

links_1 = soup.find_all("a") #a태그들을 모두 link변수에 담는다.
print('find_all 타입: ', type(links_1)) #결과: <class 'bs4.element.ResultSet'>
print(links_1)
    #결과: [<a href="http://www.naver.com">naver</a>, <a href="http://www.daum.net">daum</a>, <a href="https://www.google.com">google</a>, <a href="https://www.tistory.com">tistory</a>]

links1 = soup.find("a") #첫번째 a태그만 담는다.
print('find 타입: ', type(links1)) #결과: <class 'bs4.element.Tag'>
print(links1)
    #결과: <a href="http://www.naver.com">naver</a>
print(links1.string) #결과: naver
print(links1.attrs['href']) #결과: http://www.naver.com

for a in links_1:
    print('a:', type(a), a)
            #a: <class 'bs4.element.Tag'> <a href="http://www.naver.com">naver</a>
            #a: <class 'bs4.element.Tag'> <a href="http://www.daum.net">daum</a>
            #a: <class 'bs4.element.Tag'> <a href="https://www.google.com">google</a>
            #a: <class 'bs4.element.Tag'> <a href="https://www.tistory.com">tistory</a>
    print(a.string) #text: naver
    print(a.attrs['href']) #href: http://www.naver.com


links_2 = soup.find_all("a", string="daum")
print('links_2:',links_2)

links_3 = soup.find_all("a", limit=3) #3개만 갖고온다.
print('links_3:',links_3)

links_4 = soup.find_all(string=["naver","google"])
print('links_4:',links_4)

#links_1 = soup.find_all("a") #처럼 모든 a태그를 link변수에 담는데 이는 실전에서 너무 복잡할 수 있다.
