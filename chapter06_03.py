# Chapter06-3
# 파이썬 패키지
# 패키지 작성 및  사용법
# 패키지 : 모듈이 뭉쳐져있는 폴더
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# 상대경로 : ..(부모 디렉토리) .(현재 디렉토리)

# __init.py__ : Python 3.3 부터는 없어도 패키지로 인식! 단, 하위 호환을 위해 작성하는 것을 추천!
# __init.py__ 에서 __all__ = ['module3'] 이라고 해놓았을 경우, module1은 쓸 수 없다.
# 즉, 해당 리스트에 추가해주고 사용을 허락해야 함


# 예제1
# 같은 경로
# import sub.sub1.module1
# import sub.sub2.module2

# 사용
# sub.sub1.module1.mod1_test1()
# sub.sub1.module1.mod1_test2()
#
# sub.sub2.module2.mod2_test1()
# sub.sub2.module2.mod2_test2()

print()
print()
print()

# 예제2
# from 어디서 부터 가져올껀데?
from sub.sub1 import module1
from sub.sub2 import module2 as m2  # alias

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print()
print()
print()

# 예제 3
from sub.sub1 import *  # 전부 다 가져와! 자주 사용은 비추천 안쓰는 모듈까지 가져올 필요 x 메모리 낭비

module1.mod1_test1()
module1.mod1_test2()
