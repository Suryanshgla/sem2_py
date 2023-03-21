lst = []
even = []
odd = []
n = int(input("ENTER LIMIT"))
for i in range(0,n):
    elem  = int(input())
    lst.append(elem)
for i in range(0,n):
    if(lst[i]%2==0):
        even.append(lst[i])
    else:
        odd.append(lst[i])
print(even)
print(odd)
