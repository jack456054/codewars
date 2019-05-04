def solution(n):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = ''
    remain = n % 1000
    digit = n // 1000
    result = result + 'M' * digit


if __name__ == '__main__':

    print(solution(1), 'Should be: I')
    print(solution(4), 'Should be: IV')
    print(solution(6), 'Should be: VI')
    print(solution(14), 'Should be: XIV')
    print(solution(21), 'Should be: XXI')
    print(solution(89), 'Should be: LXXXIX')
    print(solution(91), 'Should be: XCI')
    print(solution(984), 'Should be: CMLXXXIV')
    print(solution(1000), 'Should be: M')
    print(solution(1889), 'Should be: MDCCCLXXXIX')
    print(solution(1989), 'Should be: MCMLXXXIX')
