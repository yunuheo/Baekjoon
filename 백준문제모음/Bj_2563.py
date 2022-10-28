bigPaper = [[0]*100 for i in range(100)] #arr = [[0]*열의개수 for i in range(행의개수)]

for _ in range(int(input())):             #종이의 수
    m, n = map(int, input().split(' '))   #시작좌표
    for i in range(m,m+10):               #종이의 가로,세로 = 10
        for j in range(n, n+10):
            bigPaper[i][j] = 1            #임의의 좌표 하나의 넓이가 1이기 때문에 => 10x10만큼 1로 채움

result = 0
for i in range(100):                      #도화지 전체의 1의 합 = 전체 색종이의 넓이
    for j in range(100):
        result += bigPaper[i][j]

print(result)
