# Chapter03-3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서o 중복o 수정o 삭제o)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Cap']
e = [1000, 10000.1 , ['A', 'B', 'C', 'D']]
f = [21.42, 'foo', 3, False, { 'key': 'value' }]
print(len(c)) # 시퀀스 형

# 인덱싱
print('>>>>>>>')
print('d - ', type(d), d)
print('d - 1 =', d[1])
print('d - index 0 + index 1 =', d[0] + d[1])
print('d -', d[-1])
print('e -', e[-1][0]) # e - ['B', 'a', 's', 'e']

# 문자열을 리스트로
print('e -', list(e[-1][1]))

# 슬라이싱
print('>>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', d[-2:])
print('e - ', e[-1][1:3])
print('e - ', e[-1][::2])

# 리스트 연산
print('<<<<<<<<<')
print('c + d', c + d) # [70, 75, 80, 85, 1000, 10000, 'Ace', 'Base', 'Cap']
print('c * 3', c * 3) # c * 3 [70, 75, 80, 85, 70, 75, 80, 85, 70, 75, 80, 85]
print("'Test'  + c[0]", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])

# Identity(id)
temp = c
print(temp, c)
print(id(temp)) # 4555316288
print(id(c)) # 4555316288

# 리스트 수정, 삭제
print('>>>>>>>>>>')
c[0] = 4
print(c) # [4, 75, 80, 85]

c[1:2] = ['a', 'b', 'c'] # [4, 'a', 'b', 'c', 80, 85]
print(c)

c[1] = ['a', 'b', 'c']
print(c) # [4, ['a', 'b', 'c'], 'b', 'c', 80, 85] 중첩

c[1:3] = []
print(c) # [4, 'c', 80, 85]

del c[2]
print(c) # [4, 'c', 85]

# 리스트 함수
t = [5, 2, 3, 1 ,4]
# t[5] = 10 값이 추가되지 않음

t.append(6)
t.sort() # 오름차순
t.reverse() # 배열 뒤집기

# 인덱스를 가져오는 함수
print(t.index(3), t[3]) # 동일함

t.insert(2, 7) # 인덱스 2번 자리에 7을 넣음
print(t)
t.sort(reverse=True)
print(t)
# del
t.remove(2) # [7, 6, 5, 4, 3, 1]
print(t)

p = t.pop()
print(p, t)

print(t.count(3)) # t에 3의 갯수가 몇개 있는가?

ex = [8, 9]
t.extend(ex)
print(t)

t.sort()

while t:
    data = t.pop()
    print(data)
