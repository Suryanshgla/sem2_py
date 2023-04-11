st = input()
d = {}
for i in range(len(st)):
    count = 0
    for j in range(len(st)):
        if(st[i] == st[j]):
            count = count + 1
    d[st[i]] = count
print(d)
