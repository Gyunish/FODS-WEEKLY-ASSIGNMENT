#making a function to count uppercase and lowercase letters
def counter(s):
    upper_case=0
    lower_case=0
    for char in s:         #runs the loop for every character in string
        if char.isupper():      #checks if the character is uppercase
            upper_case+=1
        elif char.islower():    #checks if the character is lowercase
            lower_case+=1
    print("The number of uppercase is:",upper_case)
    print("The number of lowercase is:", lower_case)

#taking user input
string=input("Enter a string:")

#calling function
counter(string)
