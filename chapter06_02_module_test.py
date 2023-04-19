# 모듈 사용 실습

import sys

# print(type(sys.path), sys.path)  # <class 'list'>

# 모듈 경로 삽입(일시적 등록)
# 모듈의 영구적인 등록은 검색해서 확인!
# sys.path.append('C:/Users/USER/Desktop')

# print(sys.path)

# import test_module

# print(test_module.power(10, 3))

import chapter06_02
from chapter06_02 import add

print(chapter06_02.power(10, 3))
print(add(9, 1))

