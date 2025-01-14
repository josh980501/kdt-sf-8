# MRO

class A:
    def speak(self):
        print("A 클래스")

class B(A):
    def speak(self):
        print("B 클래스")

class C(A):
    def speak(self):
        print("C 클래스")

class D(B, C): # D는 다중상속
    pass # 아무것도 안하는 키워드. 쓸거 없을때

d = D()
#A, B, C 클래스 모두 speak() 메서드를 가지고 있는데, 여기서 과연 어떤 클래스의 speak() 가 호출?
# -> MRO 원칙에 따른 클래스의 메서드가 호출이 됨
d.speak() # B 클래스
print(D.mro()) # D -> B -> C-> A -> object 순서

# 다중 상속의 유의점
# 이름이 충돌 문제가 있다.
# 상속 순서도 의도에 맞게 설정하자. ex. class D(B, C) <--요 순서

