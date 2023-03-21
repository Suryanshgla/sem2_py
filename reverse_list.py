lst = []
n = int(input("enter limit"))
for i in range(0,n):
    lst.append(input())
print(lst)
for i in range(0,n//2):
    c = lst[i]
    lst[i] = lst[n-1-i]
    lst[n-1-i] = c
print(lst)
