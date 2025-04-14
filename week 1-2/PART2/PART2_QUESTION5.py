#taking input from user
principle=float(input("Enter the principal amount"))
rate=float(input("Enter the rate of interest in percentage"))
time=float(input("Enter the time period in years"))

#calculating simple interest
simple_interest=(principle*rate*time)/100

print("The simple interest is",simple_interest)