#taking input from the user
a=int(input("Enter a number"))
b=int(input("Enter another number"))

#checking if the second number is 0
if b==0:
    print("Cant divide by 0")
else:
    result=float(a/b)
    result="%.2f"%result     #reducing to 2 decimal places
    print("The result of the first number being divided by the second is",result)