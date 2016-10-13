#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task_02 docstring"""


def bool_to_str(bval):
    """A fuction returns a 'Yes' or 'No' value to argument.

    Args:
        bval(boolean): A boolean value identify true or false.

    Returns:
        str: A value of 'Yes' or 'No'.

    Examples:
        >>>bool_to_str(1)
        'Yes'
    """

    if bval:
        string = 'Yes'
    else:
        string = 'No'
    return string
