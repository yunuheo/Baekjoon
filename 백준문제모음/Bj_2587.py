arr= []
for _ in range(5):
    arr.append(int(input()))

sum = 0
for i in range(5):
    sum += arr[i]

avr = sum//5
print(avr)

arr.sort()
print(arr[2])
