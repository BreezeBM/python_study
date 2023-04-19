# Chapter06-1
# 파이썬 클래스
# OOP 객체 지향 프로그래밍 / 인스턴스 메소드 / 인스턴스 변수

class Dog:
    species = 'firstdog'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)


# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)

# 메서드 호출
print(c.info())
print(d.info())

# 메서드 호출
print(c.speak('bow'))
print(d.speak('wow'))