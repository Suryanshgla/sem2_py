n = int(input())
c = 1
while(c <= n):
    count = 0
    for i in range(2, c):
        if(c%i==0):
            count = count + 1
    if(count == 0):
        print(c)
    c = c + 1
