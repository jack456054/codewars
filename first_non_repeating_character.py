from collections import OrderedDict


def first_non_repeating_letter(string):
    # your code here
    result_dict = OrderedDict()
    for c in string:
        if c.lower() in result_dict:
            result_dict[c.lower()] += 1
        elif c.upper() in result_dict:
            result_dict[c.upper()] += 1
        else:
            result_dict[c] = 1
    for key, value in result_dict.items():
        if value == 1:
            return key
    return ''
