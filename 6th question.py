list_a = ["car", "place", "tree", "under", "grass", "price"]

#removing letter contaning a and A using lamda function
remove_items_containing_a_or_A = lambda list_a: [x for x in list_a if not ('a' in x.lower())]
print(remove_items_containing_a_or_A(list_a))
