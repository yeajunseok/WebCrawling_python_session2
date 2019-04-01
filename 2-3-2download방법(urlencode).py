import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위에 4줄 한이유는 Atom에서 한글을 출력하지 못하기 떄문에 문제 해결하기 위해 설정한다.

import urllib.request
from urllib.parse import urlencode #urllib.parse 중에서 urlparse룰 갖고온다.

API = "https://api.ipify.org"

values = {
    'format':'json'
}
print('이전:',values) #이전: {'format': 'json'}
params = urlencode(values)
print('이후:',params) #이후: format=json

url = API + "?" + params
print("요청 url:",url) #요청 url: https://api.ipify.org?format=json

reqData = urllib.request.urlopen(url).read().decode('utf-8')
print("결과값:",reqData) #결과값: {"ip":"59.29.245.38"}
