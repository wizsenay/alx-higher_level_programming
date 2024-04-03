#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range*list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            dive = 0
        except ZeroDivisionError:
            print("division by 0")
            dive = 0
        except IndexError:
            print("out of range")
            dive = 0
        finally:
            new_list.append(div)
    return new_list
