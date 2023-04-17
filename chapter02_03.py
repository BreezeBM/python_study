# Chapter02-3
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n)) # <class 'int'>
print()

# 동시 선언
x = y = z = 300
print(x, y, z)
print()

# 선언
var = 75
print(var) # 75
print(type(var)) # <class 'int'>

# 재선언
var = 'change value'
print(var) # change value
print(type(var)) # <class 'str'>

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력
# * 예시 2번 으로 설명을 하면, class 'int' 형을 만들고 777을 넣어서 콘솔에 출력됨

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777
n = 777
print(n, type(n))
print()

m = n
# m -> 777 <- n
print(m, n)
print(type(m), type(n))

m = 400
print(m, n)
print(type(m), type(n))
print()

# id(identity)확인: 객체의 고유값 확인
m = 800
n = 655

print(id(m)) # 4450091888 -> 오브젝트의 고유값
print(id(n)) # 4450091984
print(id(m) == id(n)) # False
print()

# ! 파이썬의 최적화 : 같은 오브젝트를 참조
# 똑같이 300을 할당해서 이 값은 똑같음
# 파이썬 입장에서는 이 300을
# 니가 나중에 복사해서 써도 되는데 굳이 지금부터 똑같은 값을
# 이렇게 할당해서 쓰는 것을 비효율적이라고 판단해서, 이 값은 하나의 같은 인스턴스이다.
m = 300
n = 300
o = 300
p = 300

print(id(m)) # 4432221392 -> 오브젝트의 고유값
print(id(n)) # 4432221392
print(id(m) == id(n)) # True
print()

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# Snake Case : number_of_college_graduates

# 예약어는 변수명으로 불가능
"""
False def if raise
None del import return
True elif in try
and else is while
as except lambda with
assert finally nonlocal yield
break for not
class from or
continue global pass
"""
