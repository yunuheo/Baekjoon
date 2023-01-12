'''
문제링크: https://www.acmicpc.net/problem/11650
'''

# 점의 개수 N을 입력받는다.
n = int(input())

arr = []
# N개의6 좌표를 입력받아 2차원리스트를 만들자.
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()

for i in range(n):
    print(arr[i][0],arr[i][1])
        