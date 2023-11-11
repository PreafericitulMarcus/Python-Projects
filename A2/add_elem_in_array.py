# finished


def test_add1():
    """
    Desc:  tests function add1
    Data: the main list and a value to add
    Precondition: from_main_list - list, value_add1 - natural number
    Result: Nothing if everything works, error otherwise
    """
    assert add1([2, 3, 4], 5) == [2, 3, 4, 5], "error2"
    assert add1([10, 9, 8], 7) == [10, 9, 8, 7], "error3"

def add1(lst_add1, value_add1):
    """
    Desc: adds element in list
    Data: lst_add1 - list, value_add1 - natural number
    Result: list + value to add
    """
    lst_add1.append(value_add1)
    return lst_add1


def test_add2():
    """
    Desc:  tests function add3
    Data: the main list, an index to add the element to and a value to add
    Precondition: from_main_list - list,index - natural number value_add1 - natural number
    Result: Nothing if everything works, error otherwise
    """
    assert add2([2, 3, 4], 1, 5) == [2, 5, 3, 4], "error2"
    assert add2([10, 9, 8], 2, 7) == [10, 9, 7, 8], "error3"


def add2(lst_add2, index_to_add_to, value_add2):
    """
    Desc: adds element in list at certain index
    Data: lst_add2 - list, index_to_add_to - natural number, value_add2 - natural number
    Result: list where at index_to_add_to is value_add2
    """
    new_lst = []
    for i in range(len(lst_add2)):
        if i == index_to_add_to:
            new_lst.append(value_add2)
        new_lst.append(lst_add2[i])
    return new_lst
