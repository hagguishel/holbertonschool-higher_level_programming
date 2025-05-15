#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for number in my_list:
        if number == search:
            new_list.append(replace)
        else:
            new_list.append(number)
    return new_list
