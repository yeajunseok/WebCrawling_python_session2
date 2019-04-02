import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위에 4줄 한이유는 Atom에서 한글을 출력하지 못하기 떄문에 문제 해결하기 위해 설정한다.
from bs4 import BeautifulSoup

fp = open("food-list.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

#CSS선택자로~
#다양한 예제로 뽑을수 있다.
print("1", soup.select_one("li:nth-of-type(1)").string)
print("2", soup.select_one("#ac-list > li:nth-of-type(4)").string)
print("3", soup.select("#ac-list > li[data-lo='cn']")[0].string) #select는 list형태로 반환한다.
print("4", soup.select("#ac-list > li.alcohol.high")[0].string)
print("44", soup.select("#ac-list > li[class='alcohol']")[1].string) #select는 list형태로 반환한다.

param = {"data-lo":"cn", "class":"alcohol"}
print("5", soup.find("li",param).string)
print("6", soup.find(id="ac-list").find("li",param).string)

for ac in soup.find_all("li"):
    if ac['data-lo'] == 'us':
        print('data-lo == us', ac.string)
