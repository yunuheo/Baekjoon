C = int(input())   #테스트케이스의 수

for _ in range(C):
  Scores = list(map(int,input().split()))  #각 학생의 점수를 리스트에 저장
  average = 0
  Students = Scores[0]
  #average = sum(scores[1:])/scores[0] ==> *중요* for문 대신 sum함수의 인자로 리스트를 넣어 평균을 구할 수 있음!! 
  for i in Scores[1:]:   #평균 구하는 for문
      average += Scores[i]
  average /= Students
  
  cnt = 0
  for j in range(Students):   #평균이넘는 학생들의 비율을 구하자 /// *중요* range함수 for i in Scores[1:] 형태로 사용할 수도 있음 이때 하위 if문은 단순히 i로 참조
    if  Scores[j+1] > average:  #첫번째 값은 학생의수 => 1번 인덱스부터 비교해야함!
      cnt += 1
  rate = (cnt/Students)*100
  print('%.3f%%' %rate)   #문자열'%'을 출력학 위해 연속해서 써줌(%%)
 
