#그룹단어는  문자가 단독으로 나오거나 연속해서 나와야함.
#따라서 같은 문자 사이에는 다른 문자가 와서는 안됨.
list = []
N = int(input())
for _ in range(N):
    list.append(input())
