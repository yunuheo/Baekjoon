#간단한 별찍기 문제

N = int(input())

for i in range(N):
    print((' '*((N-1)-i))+('*'*(i+1)))