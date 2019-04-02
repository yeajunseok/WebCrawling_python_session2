import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위에 4줄 한이유는 Atom에서 한글을 출력하지 못하기 떄문에 문제 해결하기 위해 설정한다.

import urllib.request
from urllib.parse import urlparse #urllib.parse 중에서 urlparse를 갖고온다.

print(urlparse("www.naver.com")) #ParseResult(scheme='', netloc='', path='www.naver.com', params='', query='', fragment='')

######################
# 다양한 urllib.request.urlopen(url).000() 결과값
url = "http://www.encar.com"
mem = urllib.request.urlopen(url)
#print(mem) #결과값: <http.client.HTTPResponse object at 0x00000122130F1518>
#print(type(mem)) #결과값: <class 'http.client.HTTPResponse'>
#print("geturl : ", mem.geturl()) #geturl :  http://www.encar.com/index.do
#print("status : ", mem.status) #결과: 200, 200은 정산, 404은 없음, 403은 거절당함, 500은 서버애러.
#print("code : ", mem.getcode())
#print("info : ", mem.info())
#print("headers : ", mem.getheaders()) #리스트형태로 나온다.
#print("read : ", mem.read(10)) #숫자만큼만 읽어온다.
#print("read : ", mem.read())
#print("read : ", mem.read(50).decode("utf-8")) #euc-kr
