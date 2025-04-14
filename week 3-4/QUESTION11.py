#making 3 dictionaries
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}

#combining the 3 dictionaries into one
nums={**dic1,**dic2,**dic3}
print("Combined dictionary:",nums)

#adding new key/value pair (7,10)
nums[7]=70
print("After adding new key/value pair:",nums)

#updating item with key 3 to 80
nums[3]=80
print("After updating:",nums)

#removing third item from dictionary
del nums[3]
print("After deleting:",nums)

#sum of all items
sum_items=sum(nums.values())
print("Sum of all items:",sum_items)

#product of all items
product=1
for value in nums.values():
    product*=value
print("Product of all items:",product)

#maximum and minimum
max_value=max(nums.values())
min_value=min(nums.values())
print("Maximum value:",max_value)
print("Minimum value:",min_value)
