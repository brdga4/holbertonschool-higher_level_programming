#!/usr/bin/python3

def uniq_add(my_list=[]):
    if len(my_list) == 1:
        return (my_list[0])
    sum = 0
    sorted_list = sorted(my_list)
    for i in range(len(sorted_list)):
        if i == len(sorted_list) - 1:
            if sorted_list[i] == sorted_list[i - 1]:
                continue
            else:
                sum += sorted_list[i]
        elif sorted_list[i] == sorted_list[i + 1]:
            continue
        else:
            sum += sorted_list[i]
    return (sum)
