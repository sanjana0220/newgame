t_1 = (1, 4, 9, 16, 25, 36)
print(f"t_1:{t_1}")

#modified tuple 
t_modified=tuple(i*i for i in t_1)
print(f"t_modified:{t_modified}")

#Element at index 4
element_at_4=t_modified[4]
print("Element at index position 4 of t_modified:",element_at_4)

#Sliced tuple 
t_sliced=t_modified[1:4]
print(f"t_sliced:{t_sliced}")