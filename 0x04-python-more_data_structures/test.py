#!/usr/bin/python3
multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

my_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }
new_dict = multiply_by_2(my_dict)
print_sorted_dictionary(my_dict)
print("xx")
print_sorted_dictionary(new_dict)
