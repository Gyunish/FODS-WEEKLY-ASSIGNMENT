#making a function to check whether a number is armstrong or not
def is_armstrong(num):
    temp=num   #storing the number in temporary variable
    num_digits=len(str(num))    #finding the number of digits in the number
    sum=0
    while temp!=0:
        remainder=temp%10   #individual digit of the number is stored in remainder
        sum+=remainder**num_digits  #the digit is raised to the power of number of digits and added
        temp//=10   #floor division is used to not have decimal values
    if sum==num:
        return True
    else:
        return False

number=int(input("Enter a number:"))
if is_armstrong(number):
    print("The number is armstrong")
else:
    print("The number is not armstrong")
