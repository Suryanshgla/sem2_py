lst  = []
n = int(input("ENTER THE LIMIT : "))
for i in range(0,n):
    lst.append(int(input()))
c = int(input("ENTER TO  ELEMENT : "))
count = 0
for i in range(0,n):
    if(lst[i] == c):
        count = count + 1
print("%d : %d"%(c,count))
