X = int(input())
# 1/1 => 1/2,2/1 => 3/1,2/2,1/3 => 1/4,2/3,3/2,4/1 ... 과 같이 
#블록안의 분수의 개수를 n이라고 했을때 1+2+3+4+.. 처럼 늘어나는 것을 알 수 있다.

n = 1                 
while True:   #몇번째 블록안에 있는지 등차수열 규칙을 사용하여 확인(n번째)
    if (n*(n+1))/2 >= X:
        break
    n += 1


in_block_n = X - (n*(n-1))//2  #n번째 블록안에서 몇번째인가? => X번째 분수(입력값) - 이전 블록안의 분수의 갯수

a = 0
b = 0
for i in range(in_block_n):  #홀수번째 블록일때와 짝수번째 블록일때가 분모 분자가 반대임 => if-else로 구분해줌

  if n % 2 != 0:
      a = ((n*(n+1))//2)-((n*(n-1))//2) - in_block_n +1
      b = in_block_n
  
  else:
      a = in_block_n
      b = ((n*(n+1))//2)-((n*(n-1))//2) - in_block_n +1

print('%d/%d'  %(a,b))  #분수형태로 출력