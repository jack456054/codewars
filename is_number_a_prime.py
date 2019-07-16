import math


def is_prime(num):
    factor = 0
    if num <= 1:
        return False
    iter = int(math.sqrt(num))
    for i in range(2, iter + 1):
        if num % i == 0:
            factor += 1
    return True if factor == 0 else False


if __name__ == "__main__":
    print(is_prime(0),  False, "0  is not prime")
    print(is_prime(1),  False, "1  is not prime")
    print(is_prime(2),  True, "2  is prime")
    print(is_prime(73), True, "73 is prime")
    print(is_prime(75), False, "75 is not prime")
    print(is_prime(-1), False, "-1 is not prime")
    print(is_prime(3),  True, "3  is not prime")
    print(is_prime(5),  True, "5  is not prime")
    print(is_prime(7),  True, "7  is prime")
    print(is_prime(41), True, "41 is prime")
    print(is_prime(5099), True, "5099 is prime")
    print(is_prime(4),  False, "4  is not prime")
    print(is_prime(6),  False, "6  is not prime")
    print(is_prime(8),  False, "8  is prime")
    print(is_prime(9), False, "9 is prime")
    print(is_prime(45), False, "45 is not prime")
    print(is_prime(-5), False, "-5 is not prime")
    print(is_prime(-8), False, "-8 is not prime")
    print(is_prime(-41), False, "-41 is not prime")
