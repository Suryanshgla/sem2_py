try:
    x = 5/0
except ZeroDivisionError:
    print("divison not possible")

try :
    a = int("hello")
except ValueError:
    print("String cannot be converted into int")
