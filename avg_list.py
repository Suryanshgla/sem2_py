lst = []
n = int(input("enter limit : "))
s = 0
for i in range(0,n):
    elem = int(input())
    lst.append(elem)
    s = s + elem
print(s/n)
    
