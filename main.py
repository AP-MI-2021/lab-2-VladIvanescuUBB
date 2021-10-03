import unittest


def is_prime(x):
    '''
    determina daca un numar este prim sau nu
    :param x: numar intreg
    :return: True, daca x este prim sau False in caz contrar
    '''
    if (x < 2):
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def get_largest_prime_below(n):
    """
    gaseste ultimul numar prim mai mic decat un numar dat
    :param n: numar intreg
    :return: ultimul numar prim mai mic decat n sau -1 daca nu exista un astfel de numar
    """
    if n < 3:
        return -1
    for i in range(n - 1, 1, -1):
        if is_prime(i):
            return i


class TestPrime(unittest.TestCase):
    """
        Teste pentru functia get_largest_prime_below():
    """

    def test_is_prime(self):
        """
        Test if is_prime works
        """
        assert is_prime(-5) is False
        assert is_prime(1) is False
        assert is_prime(2) is True
        assert is_prime(11) is True
        assert is_prime(25) is False

    def test_get_largest_prime_below(self):
        """
        teste pentru functia test_get_largest_prime_below():
        """
        assert get_largest_prime_below(2) == -1
        assert get_largest_prime_below(5) == 3
        assert get_largest_prime_below(20) == 19
        assert get_largest_prime_below(-10) == -1
        assert get_largest_prime_below(30) == 29
