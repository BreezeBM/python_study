# Chapter07-1
# 파이썬 예외 처리의 이해
# 예외 종류
# SynctaxError, TypeError, NameError, IndexError, ValueError, KeyError...
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)에서 발생하는 예외도 중요
# 1. 예외는 반드시 처리!!!
# 2. 로그는 반드시 남김
# 3. 예외는 던져진다.
# 4. 또는 예외 무시(좋은 방법은 아님)

# SynctaxError : 문법 오류
# print('error)
# print('error'')
# if True
#    print('error')

# NameError : 참조 없음
# a = 10
# b = 15
# print(c)

# ZeroDivisionError
# print(100 / 0)

# IndexError
# x = [14, 15, 16]
# print(x[4])
# x.pop()
# x.pop()
# x.pop()
# x.pop() # error

# KeyError
# dic = { 'name' : 'Lee', 'city' : 'Busan", 'age' : '12' }
# print(dic['hobby'])
# print(dic.get('hobby'))

# 예외 없는 것을 가정하고 프로그램을 작성 -> 런타임 예외 발생 시 예외처리(EAFP 에 작성되어 있음)

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time

# print(time.time2())

# ValueError
# x = [1, 2, 3]
# x.remove(50)

# FileNotFoundError
# f = open('test.txt')

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
# x = [1, 2]
# y = (1, 2)
# z = 'text'

# print(x + y)
# print(z + y)
# print(x + z)

# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1: 여러개 가능
# except 에러명2:
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 마지막에 실행

name = ['Kim', 'Lee', 'Park']
#
# # 예제1
# try:
#     z = 'Kim2'
#     x = name.index(z)  # 0
#     print('{} Found it! {} in name'.format(z, x + 1))
# except ValueError: # ValueError만 잡음
#     print('Not found it! - Occured ValueError!')
# else:  # 정상적으로 실행됐을 때
#     print('Ok! else.')
# finally:  # 성공이던 아니던 무조건 마지막에 실행
#     print('Finally!')
#
# print()
#
# print('pass')

# 예제 2
# try:
#     z = 'Kim2'
#     x = name.index(z)  # 0
#     print('{} Found it! {} in name'.format(z, x + 1))
# except:  # 모든 에러를 다 잡음, 예외는 알 수 있지만 어떤 에러인지 알기 힘듬 except Exception으로도 씀
#     print('Not found it! - Occured ValueError!')
# else:
#     print('Ok! else.')
#
# print()

# 예제3
# try:
#     z = 'Kim2'
#     x = name.index(z)  # 0
#     print('{} Found it! {} in name'.format(z, x + 1))
# except Exception as e:
#     print(e) # 'Kim2' is not in list 에러의 내용을 출력함
#     print('Not found it! - Occured ValueError!')
# else:
#     print('Ok! else.')
#
# print()

# 예제4
# 일부로 예외를 발생 : raise
# raise 키워드로 예외 직접 발생
try:
    a = 'Park'
    if a == 'Kim':
        print('Ok Pass')
    else:
        raise ValueError
except ValueError:
    print('ValueError!!!!')



