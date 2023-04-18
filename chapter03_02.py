# Chapter03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = 'I am Python!'
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = ""
str2_t2 = str() # 빈 문자열이 생성됨

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
# I'm Boy

print("I'm a boy") # I'm a boy
print('I\'m a boy') # I'm a boy

print('a \t b') # 탭
print('a \n b') # 줄바꿈
print('a \" \" b') # a " " b

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)

escape_str2 = "What\'s going on?"
print(escape_str2)

# 탭 줄바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)

# Raw String
# 역 슬러쉬 자체를 신경쓰지 않음
raw_s = r'D:\python\test'

print(raw_s)

# 멀티 라인 입력
# 여러줄에 걸쳐서 한번에 입력하는 것
multi_str = "안녕하세요 저는 오늘도 열심히 일을 하고 파이썬 공부를 하고 있어용가뤼~"
multi_str2 = """
String
Multi
Line
Test
"""
print(multi_str2)

# \하나 넣어주면 됨
multi_str3 = \
"""
String
Multi
Line
Test
"""
print(multi_str3)

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing?"
str_o4 = "Seoul Busan Jeju"

print(str_o1 * 3) # PythonPythonPython
print(str_o1 + str_o2) # PythonApple
print('y' in str_o1) # True y가 문자열에 포함되있니?
print('z' in str_o4) # False
print('P' not in str_o2) # True 대문자 P가 문자열에 포함이 안되어 있니?

# 문자열 형 변환
print(str(66), type(str(66))) # 66 <class 'str'>
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수
"""
upper
isalnum
startwith
count
endswith
isalpha
...
"""
str_ex1 = 'python'
print("Capitalize: ", str_ex1.capitalize()) # Capitalize:  Abcd
print("endswith?: ", str_ex1.endswith('s')) # False
print("replace", str_ex1.replace('thon', 'pi')) # replace pypi

# 문자열을 list 형태로 반환하는데, 알파벳 순서로 정렬
print("sorted: ", sorted(str_ex1)) # sorted:  ['h', 'n', 'o', 'p', 't', 'y']
print("split: ", str_o4.split(" ")) # split:  ['Seoul', 'Busan', 'Jeju']

# 반복(시퀀스)
im_str = 'Good Boy!'

print(dir(im_str)) # 콘솔에 나오는 나열되는 값중 __iter__ 가 있으면 반복이 가능함

for i in im_str:
    print(i)

# 슬라이싱 연습
str_sl = "Nice Python"

# 슬라이싱 연습
print(len(str_sl))
print(str_sl[0:3]) # 0부터 3앞까지 => 0부터 2까지만 나와라!
print(str_sl[5:]) # Python
print(str_sl[:len(str_sl)]) # Nice Python
print(str_sl[:11]) # Nice Python
print(str_sl[1:4:2]) # ie 2칸 간격으로 가져와라
print(str_sl[1:11:2])

print(str_sl[-5:]) # ython
print(str_sl[1:-2]) # ice Pyth
print(str_sl[::2]) # Nc yhn 처음 부터 2칸 간격
print(str_sl[::-1]) # nohtyP eciN 역출력

# 아스키 코드(또는 유니코드)
a = 'z'

# str -> ascii
print(ord(a)) # 122

# ascii -> str
print(chr(122)) # z
