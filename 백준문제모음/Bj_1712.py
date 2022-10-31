A,B,C = map(int,input().split(' '))

#A = 고정비용
#B = 가변비용(한대의 노트북 기준)
#C = 책정된 노트북 가격
# 손익분기점 = C의 가격

#1000+70*n < 170*n ==> A+B*n < C*n 일때의 n을 구하면 될 듯 (n은 판매량)

'''n = 1
while True:
    if C == 1 or B >= C:
        n = -1
        break
    elif A//(C-B) < n:
        break
    n += 1

print(n)
'''

if C == 1 or B >= C:
    print(-1)
else:
    print(A//(C-B)+1)   #판매량 n을 기준으로 식을 이항하여 표현(나누기 연산시 소수점을 피하기 위해 // 연산식 사용)
                        #판매량이 A//(C-B)를 넘어야 하기 때문에 1을 더해줘야함