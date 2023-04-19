# Chapter06-2
# 파이썬 모듈
# Module : 함수 변수 클래스 등 파이썬 구성 요소 등을 모아놓은 파일
def add(x, y):
    return x + y


def substact(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def power(x, y):
    return x ** y


# print('-' * 15)
# print('called inner!')
# print(add(5, 5))
# print(substact(5, 5))
# print(multiply(5, 5))
# print(divide(5, 5))
# print(power(5, 3))
# print('-' * 15)

# 지금 작성된 모듈은 import 했을 때 실행하면 프린트 구문이 전부 실행이 된다.
# 실행이 안되게 하려면 파일을 열어서 직접 print 구문을 전부 주석처리를 해야한다.
# 파이썬의 경우는 외부에서 모듈을 import해서 쓰는 경우와 자기 자신을 스스로 실행할 경우를 구분하는 예약어가 존재함

# __name__ 사용
# 외부에서 import 해서 사용하면 print가 실행이 안됨!
# 모듈 파일에서 실행하면 실행이됨! -> 즉 내 자신일 경우에만 실행

if __name__ == "__main__":
    print('-' * 15)
    print('called! __main__')
    print(add(5, 5))
    print(substact(5, 5))
    print(multiply(5, 5))
    print(divide(5, 5))
    print(power(5, 3))
    print('-' * 15)



