alphabets = input().upper()

each_alpha = list(set(alphabets))

arr = []
for i in each_alpha:
    cnt = alphabets.count(i)
    arr.append(cnt)

