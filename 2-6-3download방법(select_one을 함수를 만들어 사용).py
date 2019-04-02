import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위에 4줄 한이유는 Atom에서 한글을 출력하지 못하기 떄문에 문제 해결하기 위해 설정한다.
from bs4 import BeautifulSoup

fp = open("cars.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

def car_func(selector):
    print("car_func", soup.select_one(selector).string)

car_func("#gr")
car_func("li#gr")
car_func("ul > li#gr")
car_func("#cars #gr")
car_func("#cars > #gr")
car_func("li[id=gr]")

print("car_func",soup.select("li")[3].string)
print("car_func",soup.find_all("li")[3].string)
