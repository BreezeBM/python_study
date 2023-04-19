# Chapter05-2-ex1
# 파이썬 사용자 입력

# 에러 발생
# 이 부분을 처리를 하지 않으면 에러가 그대로 노출 됨
# n = int(input("Enter your number :"))

# 예제 1 -> 예외처리
# 6 번줄을 실행하게 되면 ValueError가 발생함.
# except는 catch의 의미
try:
    n = int(input("Enter a number : "))
    print('Your number is :', n)
except ValueError:
    print('This is not a number')

# 예제 2 -> 올바른 값 입력 완료 까지 지속
while True:
    try:
        n = int(input("Enter your number : "))
        print('Your Number Is: ', n)
        break
    except ValueError:
        print('This is not a number')