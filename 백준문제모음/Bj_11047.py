N,k = map(int,input().split(' '))

arr = []
for _ in range(N):
    arr.append(int(input()))

cnt = 0
while True:
  for _ in range(N):
    if max(arr)>k:
        arr.remove(max(arr))
  if k == max(arr):
    cnt += 1
    break
  k -= max(arr)
  cnt += 1
    


print(cnt)

