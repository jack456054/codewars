def find_even_index(arr):
    for index, _ in enumerate(arr):
        if sum(arr[:index]) == sum(arr[index + 1:]):
            return index
    return -1


if __name__ == '__main__':
    print(find_even_index([1, 2, 3, 4, 3, 2, 1]), "Should be: 3")
    print(find_even_index([1, 100, 50, -51, 1, 1]), "Should be: 1")
    print(find_even_index([1, 2, 3, 4, 5, 6]), "Should be: -1")
    print(find_even_index([20, 10, 30, 10, 10, 15, 35]), "Should be: 3")
    print(find_even_index([20, 10, -80, 10, 10, 15, 35]), "Should be: 0")
    print(find_even_index([10, -80, 10, 10, 15, 35, 20]), "Should be: 6")
    print(find_even_index(range(1, 100)), "Should be: -1")
    print(find_even_index([0, 0, 0, 0, 0]), "Should be: 0", "(Should pick the first index if more cases are valid)")
    print(find_even_index([-1, -2, -3, -4, -3, -2, -1]), "Should be: 3")
    print(find_even_index(range(-100, -1)), "Should be: -1")
