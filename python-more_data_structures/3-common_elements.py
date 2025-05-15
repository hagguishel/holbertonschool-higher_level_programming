#!/usr/bin/python3
def common_elements(set_1, set_2):
    result = set()
    for element in set_1:
        if element in set_2:
            result.add(element)
    return result
