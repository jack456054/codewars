from collections import Counter


def count(string):
    result = dict()
    for character in string:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    return result

    # better solution:
    # return Counter(string)


if __name__ == '__main__':
    print(count('aba'))
    count('')
