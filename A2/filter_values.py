# finished


def isPrime(n):  # check if prime
    if n < 2:
        return False
    if n > 2 and n % 2 == 0:
        return False
    for d in range(3, n, 2):
        if n % d == 0:
            return False
    return True


def test_filter_prime():
    """
    Desc:  tests function filter_prime
    Data: the main list in which we remove the elements which are not prime
    Precondition: from_main_list - list
    Result: Nothing if everything works, error otherwise
    """
    assert filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [
        2,
        3,
        5,
        7,
        11,
    ], "error2"
    assert filter_prime([11, 12, 14, 15, 6, 643, 643, 342, 5]) == [
        11,
        643,
        643,
        5,
    ], "error3"


def test_filter_negative():
    """
    Desc:  tests function filter_negative
    Data: the main list in which we remove the elements which are not negative
    Precondition: from_main_list - list
    Result: Nothing if everything works, error otherwise
    """
    assert filter_negative([1, 2, -3, 4, 5, 6, -7, 8, 9, 10, -11, 12]) == [
        -3,
        -7,
        -11,
    ], "error2"
    assert filter_negative([11, 12, 14, -15, 6, 643, 643, -342, 5]) == [
        -15,
        -342,
    ], "error3"


def filter_prime(lst):
    """
    Desc: deleting everything exept the prime numbers
    Data: lst - list
    Result: a list of prime numbers
    """
    for i in range(len(lst) - 1, -1, -1):
        if not isPrime(lst[i]):
            del lst[i]
    return lst


def filter_negative(lst):
    """
    Desc: deleting everything exept the negative numbers
    Data: lst - list
    Result: a list of negative numbers
    """
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] >= 0:
            del lst[i]
    return lst
