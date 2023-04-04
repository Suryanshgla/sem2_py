x = {}
n = int(input("HOW MANY ELEMENTS : "))
for i in range(n):
    k = input("Key : ")
    v = input("value :")
    x.update({k:v})
print("the dictinary is : ",x)
