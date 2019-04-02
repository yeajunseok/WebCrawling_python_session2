import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위에 4줄 한이유는 Atom에서 한글을 출력하지 못하기 떄문에 문제 해결하기 위해 설정한다.

import urllib.request

imgUrl = "https://ssl.pstatic.net/tveta/libs/1226/1226441/2e97166c1c03eb93e1ef_20190329152201980_1.jpg"

savePath1 = "c:/Users/yeajunseok/Documents/Atom/WebCrawling_python/session2/과제1_1.jpg"

urllib.request.urlretrieve(imgUrl, savePath1)

print("다운로드 완료!")
