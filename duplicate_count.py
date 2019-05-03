from collections import Counter


def duplicate_count(text):
    return sum(num > 1 for num in Counter(text.lower()).values())

# Old version:

# def duplicate_count(text):
#     dict, duplicate = {}, 0
#     text = text.lower()
#     for char in text:
#         if char not in dict:
#             dict[char] = 0
#         elif dict[char] == 1:
#             duplicate += 1
#         dict[char] += 1
#     return duplicate


if __name__ == '__main__':
    print(duplicate_count("abcde"), "Should be: 0")
    print(duplicate_count("abcdea"), "Should be: 1")
    print(duplicate_count("indivisibility"), "Should be: 1")
    print(duplicate_count("aA"), "Should be: 1")
