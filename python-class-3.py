import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위에 4줄 한이유는 Atom에서 한글을 출력하지 못하기 떄문에 문제 해결하기 위해 설정한다.

#클래스 변수, 인스턴스 변수
#클래스 네임스페이스 이해하기
class Warehouse:
    stock_num = 0 #클래스 변수는 공유가 된다.
    def __init__(self, name):
        self.name = name #인스턴스 변수: 각각의 인스턴스에 귀속된다. 공유되지 않는다.
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num += -1

user1 = Warehouse("kim")
user2 = Warehouse("Park")

print(user1.name)
print(user2.name)

print(user1.__dict__) #{'name': 'kim'}, stock_num은 없다.
print(user2.__dict__) #{'name': 'Park'}, stock_num은 없다.
print(Warehouse.__dict__) #{'__module__': '__main__', 'stock_num': 2, '__init__': <fu, #stock_num : 2가 된것에 주목하자

print(user1.stock_num) #2 ,동작이 처음에는 자신의 namespace를 확인하고 ---없다면---> class의 namespace에서 찾는다.
print(user2.stock_num) #2
