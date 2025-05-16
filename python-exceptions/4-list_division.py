#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    division = 0
    result = []

    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
            result.append(division)

        except TypeError:
            result.append(0)
            print("wrong type")

        except ZeroDivisionError:
            result.append(0)
            print("division by 0")

        except IndexError:
            result.append(0)
            print("out of range")

        finally:
            pass
    return result
