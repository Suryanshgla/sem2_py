try:
    x = 5/0
    a = int("hello")
except ValueError:
    print("String cannot be converted into int")
except ZeroDivisionError:
    print("divison not possible")
finally :
    print("above code has error")
