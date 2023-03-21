lst = []
n = int(input("ENTER LIMIT : "))
for i in range(0,n):
    lst.append(input())
print(lst)
flag  = 0
for i in range(0,n//2):
    c = lst[i]
    if(lst[i] == lst[n-1-i]):
        flag = flag + 1
    lst[i] = lst[n-1-i]
    lst[n-1-i] = c
print(lst)
if(flag == n//2):
    print("ITS A PPALINDROME")
else:
    print("ITS NOT A PALINDRONE")
