n = int(input())
for i in range(-n,n+1):
    for j in range(-n,n+1):
        if(i**2 + j**2 <= n**2 ):
            print(" #",end="")
        else:
            print("  ",end="")
    print()
