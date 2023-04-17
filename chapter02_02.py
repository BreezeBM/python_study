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

### 3가지 Format Practioes

x = 50
y = 100
text = 20230417
n = 'Thomas'

# 출력1
ex1 = 'n = %s, s = %s, sum = %d' % (n, text, (x + y))
print(ex1)

# 출력2 !!
ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n=n, s=text, sum=x + y)
print(ex2)

# 출력3 !!!
ex3 = f'n = {n}, s = {text}, sum = {x + y}'
print(ex3)
print()

# 구분 기호
m = 10000000000
print(f'm : {m:,}') # m : 10,000,000,000
print()

# 정렬
# ^ : 가운데, < : 왼쪽, > : 오른쪽

t = 20
print(f"t : {t:10}") # 10 칸을 확보해라 t :         20
print(f"t center : {t:^10}") # t center :     20
print(f"t left : {t:<10}") # t left : 20
print(f"t right : {t:>10}") # t right :         20
print()

print(f"t center : {t:-^10}") # t center : ----20---- 빈칸은 -로 채워짐
print(f"t center : {t:*^10}")
print(f"t center : {t:#<10}")
print(f"t center : {t:@>10}")


