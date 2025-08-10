# step 1: an empty list
my_list = []

# step2: appending elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# step3: inserting 15 at the second position
my_list.insert(1, 15)

# step4: extending the list with [50, 60, 70]
my_list.extend([50, 60, 70])

# step5: removing the element
my_list.pop()

# step6: sorting in ascending order
my_list.sort()

# step7: find and print the index of 30
index_30 = my_list.index(30)

print("Final List:", my_list)
print("Index of 30:", index_30)