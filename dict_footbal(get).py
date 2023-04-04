x = {}
n = int(input("HOW MANY PLAYERS : "))
for i in range(n):
    k = input("Key : ")
    v = input("value :")
    x.update({k:v})
print("the dictinary is : ",x)
name = input("PLAYER NAME : ")

#FIND THE GOALS SCORED BY THE PLAYER
goals = x.get(name,-1)
if(goals == -1):
    print("PLAYER NOT FOUND")
else:
    print("{} SCORED {} GOAL".format(name,goals))
