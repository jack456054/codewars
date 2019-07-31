import itertools


def choose_best_sum(t, k, ls):
    max_sum = -1
    for sum_num in itertools.combinations(ls, k):
        if sum(sum_num) <= t and sum(sum_num) > max_sum:
            max_sum = sum(sum_num)
    return max_sum if max_sum >= 0 else None


if __name__ == '__main__':
    xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
    print(choose_best_sum(230, 4, xs))
    print(choose_best_sum(430, 5, xs))
    print(choose_best_sum(430, 8, xs))
