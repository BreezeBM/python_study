# Chapter02-1
# how to use print

"""
\n : 개행
\t : 탭
\\ : 문자
\" : 문자
\' : 문자
\000 : null 문자
"""

# 기본 출력
print('-----기본출력-----')
print('python start!')
print("python start!")
print() # 개행
print('''python start!''')
print("""python start!""")
print('----------------')
print()

# seperator option
print('--seperator option--')
print('P', 'Y', 'T', 'H', 'O', 'N')
print('P', 'Y', 'T', 'H', 'O', 'N', sep='') # sep 어떤 기준으로 합칠까?
print('P', 'Y', 'T', 'H', 'O', 'N', sep=',')
print('010', '7777', '7777', sep='-')
print('------------------')
print()

#end option
print('---end option---')
print('Welcome to', end='') # Welcome toIT News
print('IT News', end='')
print()

print('Welcome to', end=' ') # Welcome to IT News Web Site!
print('IT News', end=' ') # end 다음 프린트 문에 어떻게 할 것인가?
print('Web Site!')
print('----------------')
print()

# file option
import sys

# print('Learn Python', file='text.txt')
print('Learn Python', file=sys.stdout)
print()

# ! format 사용 (d, s, f)
# d 정수 s 문자열 f 실수
print('%s %s' %('one', 'two'))
print('{} {}'.format('one', 'two'))
print('%s는 나이가 %d살 %s' %('철수', 3, '입니다'))
print('{1} {0}'.format('one', 'two'))
print()

# %s의 여러가지 패턴
print('%10s' %('nice')) #10개의 자리수 123456nice
print('{:>10}'.format('nice')) # 123456nice

print('%-10s' %('nice')) # nice567890
print('{:<10}'.format('nice')) # nice567890

print('{:_>10}'.format('nice')) # ______nice
print('{:$>10}'.format('nice')) # $$$$$$nice

print('{:^10}'.format('nice')) #    nice    중앙정렬

print('%.5s' %('nice'))
print('%.5s' %('pythonstudy')) # pytho .은 절삭을 한다는 의미
print('{:10.5}'.format('pythonstudy')) # pytho67890 공간은 10개이지만 5글자만 나오게 절삭
print()

# %d s와 다르게 d를 계속 붙여주어야 함
print('%d %d' %(1,2))
print('{} {}'.format(1,2))

print('%4d' %(42))
print('{:4d}'.format(42))

print('%4d' %(42234234)) # 42234234
print('%.4d' %(421234))
print()

# %f
print('%f' %(3.1241234123123)) # 3.124123
print('{:f}'.format(3.1241234123123))

# 정수부는 1자리 소수부는 18자리 나와주세요
print('%1.18f' %(3.1241234112938190223123)) # 3.124123411293818986

print('%06.2f' %(3.1241234112938190223123)) # 003.12 총 6자리 중에 소수부는 2개 나머지는 0으로 채움
print('{:06.2f}'.format(3.1241234112938190223123)) # 003.12
print()
