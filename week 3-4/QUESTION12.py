set1={20,40,60}
set2={10,20,30,40,50,60}

#finding union of set 1 and 2
union=set1|set2
print("Union of set1 and set2:",union)
print("Length of union:",len(union))

#finding intersection of set 1 and 2
intersection=set1&set2
print("Intersection of set1 and set2:",intersection)

#finding symmetric difference
symmetric_diff=set1^set2
print("Symmetric difference between set1 and set2:",symmetric_diff)

#adding 40 to set 1
set1.add(40)
print(set1)     #set 1 does not change because 40 is already present

#removing 20 from set 2
set2.remove(20)
print("Set 2 after removing 20:",set2)
