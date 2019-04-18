import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위에 4줄 한이유는 Atom에서 한글을 출력하지 못하기 떄문에 문제 해결하기 위해 설정한다.

#self 이해하기
class SelfTest():
    def function1():
        print("function1 called!")

    def function2(self):
        print(id(self))
        print("function2 called!")

f = SelfTest()
#print(dir(f))

f.function1() #오류 발생, TypeError: function1() takes 0 positional arguments but 1 was given
f.function2() #성공, 즉 자동으로 뭔가 넘어감...
print(id(f)) #3059900794248  ,  3059900794248 주소값이 일치한다.
#설명: 인스턴스의 주소값이 self에 담겨서 넘어간다. 즉,


#그렇다면 function1을 self없이 접근 하려면?
print(SelfTest.function1())
