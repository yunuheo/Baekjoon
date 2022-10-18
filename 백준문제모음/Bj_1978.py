#N개의 수 중에서 소수가 몇개인지?

N = int(input())
arr = list(map(int,input().split(' ')))

cnt = 0 
is_Sosoo = True
for i in range(0,len(arr)):
  if arr[i] == 1:
    is_Sosoo = False
    continue
  if arr[i] == 2:
    is_Sosoo == True
    cnt += 1
    continue
  else:
    for j in range(2,arr[i]):
      if arr[i] % j == 0:
          is_Sosoo = False
          break
      is_Sosoo =True

  if is_Sosoo == True:
      cnt += 1  #소수면 1을 더함
print(cnt)  

     
     
    