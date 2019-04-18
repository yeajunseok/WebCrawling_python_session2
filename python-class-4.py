import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위에 4줄 한이유는 Atom에서 한글을 출력하지 못하기 떄문에 문제 해결하기 위해 설정한다.

#클래스 변수와 인스턴스 변수 차이점 이해하기
class NameTest:
    total = 0

print(dir())

print("before : ", NameTest.__dict__) #, 'total': 0,

NameTest.total = 1

print("after : ", NameTest.__dict__) #, , 'total': 1,

n1 = NameTest()
n2 = NameTest()
print(id(n1), "vs", id(n2)) #주소값은 예상했듯 2348606080896 vs 2348606080840 다르다.
print(dir())
print(n1.__dict__) #{}, 암것도 없음
print(n2.__dict__) #{}, 암것도 없음
n1.total = 77
print(n1.__dict__) #{'total': 77}, 뭔가 생김!!!!!!!

print(n1.total) #n1은 자기 인스턴스 안에 total값이 있다.
print(n2.total) #하지만 n2는 자신의 namespace를 확인하고 --없기떄문에--> class의 namespace에서 찾는다.
