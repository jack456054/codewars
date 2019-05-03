def high_and_low(numbers):
    num = [int(integer) for integer in numbers.split()]
    return '{} {}'.format(max(num), min(num))

# # Old version:
# def high_and_low(numbers):
#     num = [int(integer) for integer in numbers.split()]
#     return str(max(num)) + ' ' + str(min(num))


if __name__ == '__main__':
    print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "Should be: 542 -214")
