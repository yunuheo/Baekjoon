A, B, V = map(int,(input().split(' ')))

Up_perDay = 0
day = 0

while True:
   
    Up_perDay +=  A-B
    
    if Up_perDay == V:
        break
    elif Up_perDay > V:
        break
    day += 1

print(day)