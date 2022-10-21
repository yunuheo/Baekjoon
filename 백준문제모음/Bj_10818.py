#N개의 정수가 주어졌을때 최솟값과 최댓값 찾기

N = int(input())
arr = list(map(int,input().split(' ')))

max = max(arr)
min = min(arr)
print(min,max)
