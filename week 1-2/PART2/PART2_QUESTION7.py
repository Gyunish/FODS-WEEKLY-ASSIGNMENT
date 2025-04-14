#taking user input
string=input("Enter a string")

#couting letters and digits using loop
letter_count=0
digit_count=0
for char in string:         #runs the loop for every character in string
    if char.isalpha():      #checks if the character is a letter or not
        letter_count+=1
    elif char.isdigit():    #checks if the character is a digit or not
        digit_count+=1

print("Letter count:",letter_count)
print("Digit count:",digit_count)