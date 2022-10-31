N,k = map(int,input().split(' '))

arr = []
for _ in range(N):
    arr.append(int(input()))

cnt = 0
for i in range(N - 1, -1, -1): #동전의 가치가 오름차순으로 주어졌으므로 range함수를 사용하여 후위연산
    if k == 0:
        break
    if arr[i] > k:
        continue    
    cnt += k//arr[i]
    k %= arr[i]
 
print(cnt)

