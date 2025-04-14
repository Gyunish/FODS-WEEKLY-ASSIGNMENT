#taking userinput and storing them in list
list1=input("Enter integers separated by commas for list 1:")
try:
    list1=[int(item.strip()) for item in list1.split(',')]      #making the string input into integer
except ValueError:
    print("Invalid input")
    exit(1)

#taking userinput and storing them in list
list2=input("Enter integers separated by commas for list 2:")
try:
    list2=[int(item.strip()) for item in list2.split(',')]      #making the string input into integer
except ValueError:
    print("Invalid input")
    exit(1)

#checking if the lengths of the lists are equal or not
if len(list1)==len(list2):
    print("The lists are of equal length.")
else:
    print("The lists are not of the equal length.")

#checking if the sums of the lists are equal or not
if sum(list1)==sum(list2):
    print("The sums of both lists are equal.")
else:
    print("The sums of the lists are not equal.")

#checking for common elements
common=set(list1)&set(list2)
if common:
    print("Common elements:",common)
else:
    print("There are no common elements.")