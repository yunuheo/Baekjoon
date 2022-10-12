N = int(input())

count_six = 666    #666이 기본값 => 1씩 더해나가면서 검사해줌
cnt = 0            #666이 들어있는 수들이 출현하는 횟수
while True:
    if '666' in str(count_six):  # (*중요*) 666을 문자열로 취급하고 증가하는 숫자의 문자열에 666이 있으면 카운팅.
        cnt += 1
    if cnt == N:
        break
    count_six += 1   #조건에 해당하지 않으면 계속해서 1씩 더해나감(순차탐색 알고리즘)

print(count_six)     #cnt가 N과 같아졌을때 여태까지 최종결과 count_six 출력

    
     
