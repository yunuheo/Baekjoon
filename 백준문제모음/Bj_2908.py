A, B = map(int,(input().split(' ')))

A = (A%10)*100 + ((A//10)%10)*10 + (A//100)//100
B = (B%10)*100 + ((B//10)%10)*10 + (B//100)//100

if A > B:
    print(A,B)
else:
    print(B,A)