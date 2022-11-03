from typing import Tuple


def convert(items: Tuple):
    tuple_list = ''

    for hobby in items:
        tuple_list = tuple_list + str(hobby.value) + ', '

    tuple_list = tuple_list.rstrip(', ')

    return tuple_list
