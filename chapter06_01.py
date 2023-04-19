# Chapter06-1
# 파이썬 클래스
# OOP 객체 지향 프로그래밍 / 인스턴스 메소드 / 인스턴스 변수

# 클래스와 인스턴스의 차이 이해
# 클래스 : 붕어빵 틀, 인스턴스 : 그틀을 가지고 찍어내는 붕어빵(우리가 코드에서 사용하는 객체)
# 네임스페이스 : 객체를 인스턴스화 할때 저장된 공간
# 클래스 변수 : 직접 접근 가능
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1
# class Dog: # object 상속
#    pass # 예약어

# class Dog(object):
#    pass

# 소프트웨어 구현 대상을 클래스라고 함
# 파이썬에서 클래스가 초기화 될 때, 반드시 한번 호출되는 함수가 있다.
# __init__(self, name, age)이 호출이 되고, self가 넘어오고, 클래스를 가지고 사용할 변수를 이후 매개변수로 지정할 수 있다.
class Dog:
    # 클래스 속성
    species = 'firstdog'

    # 초기화 / 인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 클래스 정보
# print(Dog)  # <class '__main__.Dog'>

# 인스턴스화
a = Dog("dong_gu", 2)
b = Dog("baek_gu", 3)
c = Dog("dong_gu", 2)

# print(a) # <__main__.Dog object at 0x000001D07918F1C0>
# print(b) # <__main__.Dog object at 0x0000021D42103F10>
# print(c) # <__main__.Dog object at 0x0000022F49973EE0>

# a와 c의 인스턴스를 서로 다른 객체로 인식
# print(a == b, id(a), id(b), id(c)) # False 2599836794832 2599836794640 2402121367264

# 네임스페이스
# 특정한 객체를 '이름'에 따라 구분할 수 있는 범위
# 파이썬 내부의 모든 것들은 전부 객체로 구성되어 있고, 이들은 특정 이름들과의 매핑 관계를 가지고 있음
# 이 매핑을 포함하고 있는 공간을 네임스페이스라 함
# 내부적으로 키, 값 구조를 가지고 있음
print('a name space', a.__dict__)
print('b name space', b.__dict__)

# 인스턴스 속성 확인
if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.age))

print(Dog.species)
print(a.species, b.species)


# 예제2
# self의 이해
# 나만의 인스턴스의 속성

# __init__이 없으면 파이썬에서 내부적으로 클래스를 만들 때 실행해줌
class SelfTest:
    # 클래스 메서드
    def func1():
        print('func1 called')

    # self는 인스턴스를 요구함
    # 인스턴스 메서드
    def func2(self):
        print(self)
        print('Func2 called')


# self가 넘어간다는 것은 self.name, self.age와 같은 나만의 독립적에 있는 속성값에 접근이 가능
# 그 속성을 활용할 수 있음

# func1과 같은 함수는 클래스 메서드 임, 매개변수가 없기 때문에
# func2는 인스턴스 메서드 임, 인스턴스를 넘겨주던가 해야함

f = SelfTest()

print(dir(f))
print(id(f))

# f.func1() # 에러
f.func2()  # 클래스를 생성한 인스턴스화 시킨 변수가 self로 넘어감
SelfTest.func1()
# SelfTest.func2() # 에러 발생
SelfTest.func2(f)


# 예제 3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    # 객체가 소멸할 때 자동으로 호출
    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse('Lee')
user2 = Warehouse('Kim')

print(Warehouse.stock_num)
print(user1.name)
print(user2.name)
print(user1.__dict__)  # {'name': 'Lee'} stock_num이 나오지 않음
print(user2.__dict__)  # {'name': 'Kim'}  stock_num이 나오지 않음
print('BEFORE : ',Warehouse.__dict__)
print(user1.stock_num)  # 2 warehouse dict을 찾아가서 stock num을 가져옴
# 인스턴스의 네임스페이스에 없으면, 클래스의 인스턴스에 가서 찾는 다.

del user1
print('AFTER : ',Warehouse.__dict__) # stock num 1
