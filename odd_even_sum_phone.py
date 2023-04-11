phone = input("enter no. : ")
odd = 0
even = 0
for i in range(len(phone)):
    if (int(phone[i])%2 == 0):
        even = even + int(phone[i])
    else:
        odd = odd + int(phone[i])
print("ODD : "+str(odd)+" EVEN : "+str(even))
