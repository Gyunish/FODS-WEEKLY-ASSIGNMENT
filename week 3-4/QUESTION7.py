#making a function to count the letter a/A in a list of names
def count_letter(names):
    count = 0
    for name in names:
        count += name.lower().count('a')    #making all letters lower case and counting a
    return count

names_input = input("Enter names separated by commas: ")    #taking user input and storing in a list

names_list = [name.strip() for name in names_input.split(',')]      #removing whitespace and splitting using ,
count = count_letter(names_list)
print("The count of letter 'a' is:",count)