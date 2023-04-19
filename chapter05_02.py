# Chapter05-2
# 사용자 입력 input()
# input으로 받는 기본형은 str이다.

# 예제
name = input("Enter your name :")
grade = input("Enter your grade :")
age = input("Enter your age :")

print(name, grade, age)

# 예제2
number = input('Enter number :')
name = input('Enter name :')

print('type of number :', type(number)) # input으로 받는 기본형은 str이다.
print('type of name :', type(name))

# 예제3
first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))

print(first_number + second_number)

# 예제4
first_float = float(input("Enter float number : "))
second_float = float(input("Enter float number : "))

print(first_float + second_float)

# 예제5
print('FristName - {0}, LastName - {1}'.format(input("Enter First Name : "), input("Enter Second Name : ")))