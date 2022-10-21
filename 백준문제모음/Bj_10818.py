#N개의 정수가 주어졌을때 최솟값과 최댓값 찾기

N = int(input())
arr = list(map(int,input().split(' ')))
'''
min = arr[0]
max = arr[0]
for i in range(N):
    if min > arr[i]:
        min = arr[i]

for i in range(N):
    if max < arr[i]:
        max = arr[i]

print(min,max)
'''

max = max(arr)
min = min(arr)
print(min,max)
