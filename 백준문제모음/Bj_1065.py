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
arr = list(map(int, range(1,N+1)))

hansoo_cnt = 0
for i in range(N-1):
    if arr[i] < arr[i+1]:
        if (arr[i+1] - arr[i]) == (arr[i+2] - arr[i+1]):
            hansoo_cnt += 1
    else:
        if (arr[i]-arr[i+1]) == (arr[i+1]-arr[i+2]):
            hansoo_cnt += 1
print(hansoo_cnt)