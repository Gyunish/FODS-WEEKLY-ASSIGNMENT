#making a function to sort a list
def arrange(name_list):
    return sorted(name_list)    #returns the list of names sorted in alphabetical order

name_input=input("Enter names separated by commas: ")
try:
    name_list=[name.strip() for name in name_input.split(',')]  #creates a list by stripping whitespace from each name
except ValueError:
    print("Please ensure you the names are separated by commas.")
    exit(1)
sorted_list=arrange(name_list)
print("Sorted names:", sorted_list)
