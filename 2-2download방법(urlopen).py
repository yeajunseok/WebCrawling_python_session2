import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위에 4줄 한이유는 Atom에서 한글을 출력하지 못하기 떄문에 문제 해결하기 위해 설정한다.

import urllib.request

imgUrl = "http://imgnews.naver.net/image/002/2017/03/13/0002026985_001_20170313153101670.jpg"
htmlUrl = "https://google.com"

savePath1 = "c:/Users/yeajunseok/Documents/Atom/WebCrawling_python/session2/test1.jpg"
savePath2 = "c:/Users/yeajunseok/Documents/Atom/WebCrawling_python/session2/gogle.html"

f = urllib.request.urlopen(imgUrl).read() #우리의 하드디스크에 저장되기 전에 변수에(메모리)저장 시킨다.
f2 = urllib.request.urlopen(htmlUrl).read()

#위에서 read하고 여기서 write한다.
savefile1 = open(savePath1, 'wb') #w : write, r : read, a : add / b: 바이너리로
savefile1.write(f)
savefile1.close()

#위 방법보다 with문을 사용하는것이 좋다. 왜냐하면 with문은 자동으로 close를 해주기 때문이다.
with open(savePath2, 'wb') as savefile2:
    savefile2.write(f2)

print("다운로드 완료!")

"""
download2-1 과 download2-2에서 urlretrieve과 urlopen의 차이점!!! 중요함!!
urlopen은
    변수(메모리)에 먼저 할당하고 -> 파싱 -> 저장
 urlretrieve는
    바로 다이렉트로 다운받는다.(주소를 내가 정한 경로에 바로 저장한다)

* 파싱이 필요없는 데이터(이미지, 엑셀, 여러문서 한번에 다운받때)는 urlretrieve를 사용하자.
* 중간에서 필요로하는 것을 분석할때 urlopen을 사용하자.
"""
