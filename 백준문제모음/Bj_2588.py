num1 = int(input())
num2 = int(input())

a = num1*(num2%10)
b = num1*((num2//10)%10)
c = num1*(num2//100)
d = a+(b*10)+(c*100)

print(a)
print(b)
print(c)
print(d)





