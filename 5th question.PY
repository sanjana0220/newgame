frozen_set_1=frozenset({'A','B','C','D'})
frozen_set_2=frozenset({'A',2,'C',4})
print("Frozen_set_1:",frozen_set_1)
print("Forzen_set_2:",frozen_set_2)

#Union frozenset
frozenset_union=frozen_set_1.union(frozen_set_2)
print("Frozenset_union:",frozenset_union)

#Common frozen
frozenset_common=frozen_set_1.intersection(frozen_set_2)
print("Frozenset_common:",frozenset_common)

#Diffrence in forzenst
frozenset_difference=frozen_set_1.difference(frozen_set_2)
print("Frozenset_diffrence:",frozenset_difference)

#Distinct Frozenset
frozenset_distinct=frozen_set_1.symmetric_difference(frozen_set_2)
print("Forzenset_distinct:",frozenset_distinct)