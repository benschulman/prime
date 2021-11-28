from typing import Tuple


def miller_rabin_prime(n: int, a: int) -> bool:
    """Given a number (n) and a witness (a) this function performs the miller-rabin
    primality test. If the number is found not to be prime, False is returned. If the
    given number passes the miller-rabin primality test for the given witness, True is
    returned. https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

    Args:
        n (int): The number to test it's primality
        a (int): The witness number. Must be less than n

    Raises:
        ValueError: If a >= n, n <= 1 or a <= 0

    Returns:
        bool: The result of the primality test
    """
    if a >= n:
        raise ValueError(f"Witness cannot be greater than number to test: {a} > {n}")
    
    if n <= 1:
        raise ValueError(f"Number cannot be less than 1: {n}")
    
    if a <= 0:
        raise ValueError(f"Witness cannot be less than 1: {a}")
    
    if not n % 2 == 1:
        return False

    s, d = s_d_decompose(n)

    # Primality test 1
    if pow(a, d, mod=n) == 1:
        return True

    # Primality test 2
    for r in range(0, s):
        ex = pow(2,r) * d
        if pow(a, ex, mod=n) == n - 1:
            return True
    
    return False

    
def s_d_decompose(n: int) -> Tuple[int, int]:
    """Every odd number (n) can be written in the form 2^s * d + 1. This function returns
    s and d for a given odd number n. 

    Args:
        n (int): The number to decompose

    Raises:
        ValueError: If n is not odd

    Returns:
        Tuple[int, int]: A tuple containing s and d as defined above.
    """
    if not n % 2 == 1:
        raise ValueError(f"n must be odd: {n}")

    s = 0
    n = n - 1

    while n % 2 != 1:
        s += 1
        n = n // 2
    
    d = n
    
    return (s, d)
    

prime = miller_rabin_prime(91, 10)

print(prime)