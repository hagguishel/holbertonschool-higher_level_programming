#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = set()
    for i in set_1:
        if i not in set_2:
            result.add(i)
    for x in set_2:
        if x not in set_1:
            result.add(x)
    return result
