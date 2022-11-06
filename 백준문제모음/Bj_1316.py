#그룹단어는  문자가 단독으로 나오거나 연속해서 나와야함.
#따라서 같은 문자 사이에는 다른 문자가 와서는 안됨.

N = int(input())
result = N
for _ in range(N):
    word = input()
    for j in range(0,len(word)-1):
       if word[j] == word[j+1]:
        pass  #pass => 조건이 참이면 아무것도 실행안함
       elif word[j] in word[j+1:]:
        result -= 1
        break

print(result)




