# Chapter03-1
# 숫자형

"""
int: 정수
float: 실수
complex: 복소수
bool: 불린
str: 문자열(시퀀스)
list: 리스트(시퀀스)
tuple: 튜플(시퀀스)
set: 집합
dict: 사전
"""

# 데이터 타입
str1 = "Python"
bool = True
str2 = 'Anaconda'
float_v = 10.0 # 10 == 10.0  (타입이 다름)
int_v = 7
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0
}
tuple = (7, 8, 9)
set = {7, 8, 9}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) : x의 y제곱
x ** y : x의 y제곱
"""

# 정수 선언
i = 77
i2 = -14
big_int = 77777777777777777777777777777777777777777

# 정수 출력
print(i)
print(i2)
print(big_int)

# 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산실습
i1 = 39
i2 = 939
big_int1 = 902834098203984982039410832948092834
big_int2 = 2038102984032409238490823905209384092834
f1 = 1.234
f2 = 2.345

print(i1 + i2)
print(big_int1 * i2)
print(big_int2 * i1)
print(big_int1 // i1)

# 형 변환 실습
a = 3.
b = 6 # 정수
c = .7 # 0.7
d = 12.7

print(type(a), type(b), type(c), type(d))

print(float(b)) # 6.0
print(int(c)) # 0
print(int(d)) # 12
print(int(True)) # 1, False 0
print(float(False)) # 0.0
print(complex(3)) # (3+0j)
print(complex('3')) # (3+0j)
print(complex(False)) # (3+0j)

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8) # !
print(x, y) # 몫, 나머지

# 외부 모듈
import math

print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수 6
print(math.pi)