# finished


def isPrime(n):  # check if a n is prime
    if n < 2:
        return False
    if n > 2 and n % 2 == 0:
        return False
    for d in range(3, n, 2):
        if n % d == 0:
            return False
    return True


def test_prime():
    """
    Desc:  tests function prime
    Data: the main list, an index from where we start to the search and an index where we stop the search
    Precondition: from_main_list - list, first_index and last_index - natural number
    Result: Nothing if everything works, error otherwise
    """
    assert prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2, 8) == [3, 5, 7], "error2"
    assert prime([11, 12, 14, 15, 6, 643, 643, 342, 5], 0, 8) == [
        11,
        643,
        643,
        5,
    ], "error3"


def test_odd():
    """
    Desc:  tests function prime
    Data: the main list, an index from where we start to the search and an index where we stop the search
    Precondition: from_main_list - list, first_index and last_index - natural number
    Result: Nothing if everything works, error otherwise
    """
    assert odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2, 8) == [3, 5, 7, 9], "error2"
    assert odd([11, 12, 14, 15, 6, 643, 643, 342, 5], 0, 8) == [
        11,
        15,
        643,
        643,
        5,
    ], "error3"


def prime(lst, first, last):  # creates the list of prime numbers between first and last
    """
    Desc: searching for prime numbers between indexes
    Data: lst - list, first and last - natural number
    Result: a list of prime numbers
    """
    prime_list = []
    while first <= last:
        if isPrime(lst[first]):
            prime_list.append(lst[first])
        first += 1
    return prime_list


def odd(lst, first, last):  # creates the list of odd numbers between first and last
    """
    Desc: searching for odd numbers between indexes
    Data: lst - list, first and last - natural number
    Result: a list of odd numbers
    """
    odd_list = []
    while first <= last:
        if lst[first] % 2 != 0:
            odd_list.append(lst[first])
        first += 1
    return odd_list
