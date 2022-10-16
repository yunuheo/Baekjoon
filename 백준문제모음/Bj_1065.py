#양의 정수의 각 자리가 등차수열을 이룬다면 그것을 '한수'라고 함.
'''
등차수열을 이룬다?
1~99까지는 모두 한수
각자리수가 모두 같을 경우 한수

앞자리가 큰경우 => (앞 - 뒤) 가 (뒤 - 뒤뒤)와 같는가?(반복)
앞자리가 작을경우 => (뒤 - 앞)이 (뒤뒤-뒤)와 같는가?(반복)
앞자리 뒷자리 같은 경우 => 연속해서 계속 같은가?
'''

N = int(input())

if N == 1000:  #1000은 예외로 처리
    N = 999


if N < 100:
    hansoo_cnt = N
else:
    hansoo_cnt = 99
    num = 100
    while True:
        if num == N+1:
            break
        a=list(map(int, str(num)))
        if len(a) == 3:
            if a[0] == a[1] and a[1] == a[2]:
                hansoo_cnt += 1
                num += 1
            elif a[0] > a[1]:
                if a[0]-a[1] == a[1]-a[2]:
                    hansoo_cnt += 1
                    num += 1
                else:
                    num += 1
            else: 
                if a[1]-a[0] == a[2]-a[1]:
                    hansoo_cnt += 1
                    num += 1
                else:
                    num += 1

print(hansoo_cnt)      



        

