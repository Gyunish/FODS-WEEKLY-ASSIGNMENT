#making a function to check whether a number is prime or not
def is_prime(n):
    if n<=1:        #skips 0,1 and negative numbers as they are not prime
        return False
    for i in range(2,n):    #range is 2 and n because prime numbers are only divisible by 1 and itself
        if n%i==0:
            return False
    return True

number=int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")