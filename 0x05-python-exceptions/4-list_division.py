#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    a = 0
    c = 0

    c = [0] * list_length
    while a < list_length:
        try:
            c[a] = (my_list_1[a] / my_list_2[a])
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            a += 1
    return c
