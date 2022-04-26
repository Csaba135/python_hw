my_list=[7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(my_list)
my_list_sort=sorted(my_list)
print(my_list_sort)
my_list_sort_reverse=sorted(my_list,reverse=True)
print(my_list_sort_reverse)
my_list_even=my_list_sort[1::2]
print(my_list_even)
my_list_odd=my_list_sort[::2]
print(my_list_odd)
my_list_3=my_list_sort[2::3]
print(my_list_3)