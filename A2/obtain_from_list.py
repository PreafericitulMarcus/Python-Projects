# finished


def test_sum():
    """
    Desc:  tests function sum
    Data: the main list, an index from where we start the sum and an index where we stop the sum
    Precondition: from_main_list - list, first_index and last_index - natural number
    Result: Nothing if everything works, error otherwise
    """
    assert sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2, 8) == 42, "error2"
    assert sum([11, 12, 14, 15, 6, 643, 643, 342, 5], 0, 8) == 1691, "error3"


def test_gcd():
    """
    Desc:  tests function prime
    Data: the main list, an index from where we start to the search and an index where we stop the search
    Precondition: from_main_list - list, first_index and last_index - natural number
    Result: Nothing if everything works, error otherwise
    """
    assert gcd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2, 8) == 1, "error2"
    assert gcd([11, 12, 14, 15, 6, 643, 643, 342, 5], 0, 8) == 1, "error3"


def test_max():
    """
    Desc:  tests function prime
    Data: the main list, an index from where we start to the search and an index where we stop the search
    Precondition: from_main_list - list, first_index and last_index - natural number
    Result: Nothing if everything works, error otherwise
    """
    assert maxx([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2, 8) == 8, "error2"
    assert maxx([11, 12, 14, 15, 6, 643, 643, 342, 5], 0, 8) == 643, "error3"


def sum(lst, first, last):
    """
    Desc: getting the sum between two indexes
    Data: lst - list, first and last - natural number
    Result: sum of numbers
    """
    summ = 0
    while first <= last:
        summ += lst[first]
        first += 1
    return summ


def gcd(lst, first, last):
    """
    Desc: searching for the greatest common divisor  between indexes
    Data: lst - list, first and last - natural number
    Result: the greatest common divisor
    """
    greatest_common_divisor = gcd_function(lst[first], lst[first + 1])
    for i in range(first + 2, last):
        greatest_common_divisor = gcd_function(greatest_common_divisor, lst[i])
    return greatest_common_divisor


def gcd_function(
    a, b
):  # function to determine the greatest common divisor between 2 numbers
    while b:
        r = a % b
        a = b
        b = r
    return a


def maxx(lst, first, last):
    """
    Desc: searching for the maximum number between indexes
    Data: lst - list, first and last - natural number
    Result: the maximum number between indexes
    """
    maximum = -1
    for i in range(first, last):
        if lst[i] > maximum:
            maximum = lst[i]
    return maximum
