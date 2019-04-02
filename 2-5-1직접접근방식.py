'''
2-5-1에선 직접접근이로...
2-5-3에선 tag 선택자로 직접접근하여 사용한다.
'''
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위에 4줄 한이유는 Atom에서 한글을 출력하지 못하기 떄문에 문제 해결하기 위해 설정한다.

from urllib.parse import urljoin
baseUrl = "https://test.com/html/a.html"
#print(">>", urljoin(baseUrl,"b.html")) #결과: >> https://test.com/html/b.html
#print(">>", urljoin(baseUrl,"sub/b.html")) #결과: >> https://test.com/html/sub/b.html
#print(">>", urljoin(baseUrl,"../index.html")) #결과: >> https://test.com/b.html
#print(">>", urljoin(baseUrl,"../img/img.jpg")) #결과: >> https://test.com/img/img.jpg

from bs4 import BeautifulSoup
html = """
<html><body>
  <h1>파이썬 BeautifulSoup 공부</h1>
  <p>태그 선택자</p>
  <p>CSS 선택자</p>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser') #html받는다, parser지정
#print('soup', type(soup)) #<class 'bs4.BeautifulSoup'>
#print('prettify:', soup.prettify()) #탭 이쁘게 확인하는 방법

h1=soup.html.body.h1
print('h1 type:', type(h1)) #<class 'bs4.element.Tag'> class형태임, 그리고 Tag라는 객체를 갖고왔다.
print('h1:', h1) #<h1>파이썬 BeautifulSoup 공부</h1>
print('h1:', h1.string) # 파이썬 BeautifulSoup 공부

p1 = soup.html.body.p
print('p1:', p1) # 첫번재 <p>태그 선택자</p> 태그 갖고왔다.
p2 = p1.next_sibling
print('p2:', p2) # 아무것도 없음, 그 이유는 <p>태그 선택자</p>[줄바꿈키]<p>CSS 선택자</p> 중간에 줄바꿈키 때문에 줄바꿈 키를 찾았기 때문이다.
p2_2 = p1.next_sibling.next_sibling
print('p2_2:', p2_2) # <p>CSS 선택자</p>

p3 = p1.previous_sibling.previous_sibling
print('p3:', p3) # <h1>파이썬 BeautifulSoup 공부</h1>

#그러나 next_sibling previous_sibling는 계속 크롤링 할때는 사용하지 않는다. 왜냐면 사이트가 수정되면 다른 값이 나오기 때문이다.
