#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if len(my_list) < idx < 0:
        return (my_list)
    new_list = my_list.copy()
    del new_list[idx]
    return (new_list)
