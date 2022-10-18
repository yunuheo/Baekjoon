#0층의 i호에는 i명이 산다.
'''
0층에 1호,2호,3호 => 1명, 2명, 3명 
1층에 1호 2호 3호 => 1명, 3명, 6명  
2층에 1호 2호 3호 => 1명, 4명, 10명
3층에 1호 2호 3호 => 1명, 5명, 15명
4층에 1호 2호 3호 => 1명, 6명, 21명
'''
T = int(input())

for _ in range(T):
   k = int(input())
   n = int(input())
   
   #0층은 n호까지 있고 각호는 n명이 산다.
   floor_0 = []
   for i in range(1,n+1):
   #    틀린예)floor_0[i] = i+1 => 현재 list는 Null 인데, 인덱스를 지정했으므로 에러가 난다.=> append나 insert사용
       floor_0.append(i)
   #floor_0 리스트를 층이 올라갈때마다 각호에 몇명이 살게되는지 갱신해주면 풀릴 것 같음
   for _ in range(k):
       backUp = 0
       for j in range(n):
           backUp += floor_0[j]
           floor_0[j] = backUp   #현재 list가 Null값이 아니므로 인덱스로 바로 대입해줘도 문제 없음.
   print(floor_0[n-1])
    
    


