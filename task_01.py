#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""docstring for task_01"""


def fibonacci(maxint):
    """Function to get Fibonacci series with maxium value.

    Args:
        maxint(int): An integer that serves as the upper bound of the loop.

    Returns:
        list: A series of Fibonacci numbers.

    Examples:
        >>>fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]
    """
    new_list = [0]
    lastnum, curnum = 0, 1
    while curnum < maxint:
        new_list.append(curnum)
        lastnum, curnum = curnum, lastnum + curnum
    return new_list
