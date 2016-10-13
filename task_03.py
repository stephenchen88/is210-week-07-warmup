#!/usr/bin/env python
# -*- coding utf:8 -*-
"""task_03 docstring"""


import decimal


def lexicorgraphics(to_analyze):
    """Function to get max, min, and avg for the number of words in a speech.

    Args:
        to_analyze(str): A string of sentences in a speech.

    Returns:
        tuple: Tuple with max, min and avg numbers of words in the speech.

    Examples:
        
        >>>task_03.lexicographics('''Don't stop beliveing, Hold on to that
        feeling.''')
        (5, 3, Decimal(4.0))
    """

    list_count = []
    for line in to_analyze.split('\n'):
        word_count = len(line.split(' '))
        list_count.append(word_count)

    max_words = max(list_count)
    min_words = min(list_count)
    avg_words = (decimal.Decimal(sum(count_list)))/len(count_list)
    return (max_words, min_words, avg_words)
