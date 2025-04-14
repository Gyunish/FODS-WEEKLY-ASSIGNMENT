#importing math to use the math.sqrt function
import math

#taking input from user for first coordinate
x1=float(input("Enter the x-coordinate of the first point"))
y1=float(input("Enter the y-coordinate of the first point"))

#taking input from user for second coordinate
x2=float(input("Enter the x-coordinate of the second point"))
y2=float(input("Enter the y-coordinate of the second point"))

#calculating Euclidean distance
distance=math.sqrt((x2-x1)**2+(y2-y1)**2)

print("The Euclidean distance between two coordinates is",distance)