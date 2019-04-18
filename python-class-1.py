import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위에 4줄 한이유는 Atom에서 한글을 출력하지 못하기 떄문에 문제 해결하기 위해 설정한다.

#클래스 생성자 이해하기
class UserInfo:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("----------")
        print("Name: "+self.name)
        print("Phone: "+self.phone)
        print("----------")

    def __del__(self): #객체가 사용이 안된 상태로 올라가면 가비지 컬랙터에 의해 지워지기 직전에 실행되는 코드
        print("delete!")

user1 = UserInfo("kim: ", "010-9999-8889")
user2 = UserInfo("yea: ","010-2222-3333")

print(id(user1))
print(id(user2))

user1.print_info()
user2.print_info()

print(user1.__dict__) #딕셔너리값으로
print(user2.__dict__)
print(user1.name) #딕셔너리 형태이기 때문에 이렇게 접근 가능
