alphabets = input().upper()

each_alpha = list(set(alphabets))

arr = []
for i in each_alpha:
    cnt = alphabets.count(i)
    arr.append(cnt)

if arr.count((max(arr))) >= 2:
    print('?')
else:
    print(each_alpha[arr.index(max(arr))])
