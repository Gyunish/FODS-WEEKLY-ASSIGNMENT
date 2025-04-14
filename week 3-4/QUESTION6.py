#making a function to filter a list such that only values between 1-100 are stored
def filter_int(integers):
    return [num for num in integers if 1<=num<=100]

user_input = input("Enter integers separated by commas: ")
try:
    numbers = [int(item.strip()) for item in user_input.split(',')]
except ValueError:
    print("Please ensure you enter valid integers separated by commas.")
    exit(1)
filtered=filter_int(numbers)
print("Filtered integers:",filtered)