A,B,C = map(int,input().split(' '))

#A = 고정비용
#B = 가변비용(한대의 노트북 기준)
#C = 책정된 노트북 가격
# 손익분기점 = C의 가격

#1000+70*n < 170*n ==> A+B*n < C*n 일때의 n을 구하면 될 듯

n = 1
while True:
    if C == 1 or B >= C:
        n = -1
        break
    if A+B*n < C*n:
        break
    n += 1

print(n)