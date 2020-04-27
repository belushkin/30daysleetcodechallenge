from collections import Counter

def majority_element_indexes(lst):
    """
    >>> majority_element_indexes([1,1,2])
    [0, 1]
    >>> majority_element_indexes([1,2])
    []
    >>> majority_element_indexes([])
    []
    >>> majority_element_indexes([1,1,2,2,2,2])
    [2, 3, 4, 5]
    >>> majority_element_indexes([6, 8, 1, 1, 2, 3, 8, 5, 5, 8, 8, 8, 8, 8, 8, 8])
    [1, 6, 9, 10, 11, 12, 13, 14, 15]
    >>> majority_element_indexes([2, 2, 2, 1, 1, 3, 2, 2])
    [0, 1, 2, 6, 7]
    >>> majority_element_indexes([1, 3, 2, 2, 4, 5])
    []
    """

    n = len(lst) // 2
    cnt = Counter(lst)
    return [index for index, element in enumerate(lst) if cnt[element] > n]


