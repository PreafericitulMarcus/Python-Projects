# finished


def test_remove1():
    """
    Desc:  tests function remove 1
    Data: the main list and an index
    Precondition: from_main_list - list, index - natural number
    Result: Nothing if everything works, error otherwise
    """

    assert remove1([2, 3, 4], 1) == [3, 4], "error2"
    assert remove1([10, 9, 8], 2) == [10, 8], "error3"


def test_remove2():
    """
    Desc:  tests function remove2
    Data: the main list, an index from where we start to remove and an index where we stop removing elements
    Precondition: from_main_list - list, first_index and last_index - natural number
    Result: Nothing if everything works, error otherwise
    """
    assert remove2([2, 3, 4, 5, 6, 7, 8], 1, 5) == [2, 8], "error2"
    assert remove2([10, 9, 8, 7, 6, 5, 4], 2, 4) == [10, 9, 5, 4], "error3"


def test_replace():
    """
    Desc:  tests function replace
    Data: the main list, an old variable to replace and the new variable that will replace
    Precondition: from_main_list - list, old_variable and new_variable - natural number
    Result: Nothing if everything works, error otherwise
    """
    assert replace([2, 3, 4, 5, 6, 7, 8], [2], [50]) == [50, 3, 4, 5, 6, 7, 8], "error2"
    assert replace([10, 9, 8, 7, 6, 5, 4], [5], [4]) == [10, 9, 8, 7, 6, 4, 4], "error3"


def remove1(lst, index):
    """
    Desc: removes element in list at certain index
    Data: lst_add1 - list, index - natural number
    Result: list - the element at certain index
    """
    for i in range(len(lst) - 1, -1, -1):
        if i == index:
            del lst[i - 1]
    return lst


def remove2(lst, from_index, to_index):
    """
    Desc: removes element in list between certain indexes
    Data: lst - list, from_index and to_index - natural number
    Result: list - the element between certain indexes
    """
    new_lst = []
    for i in range(len(lst)):
        if i < from_index or i > to_index:
            new_lst.append(lst[i])
    return new_lst


def replace(lst, old_value, new_value):
    """
    Desc: replaces the old values in the list with new ones
    Data: lst - list, old_value and new_value - natural number
    Result: list where the old variables are replaced with new ones
    """
    for i in range(len(lst)):
        for j in range(len(old_value)):
            if lst[i] == old_value[j]:
                lst[i] = new_value[j]
    return lst
