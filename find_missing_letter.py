def find_missing_letter(chars):
    for index, letter in enumerate(chars):
        if ord(chars[index + 1]) - ord(letter) == 2:
            return chr(ord(letter) + 1)


if __name__ == '__main__':
    print(find_missing_letter(['a', 'b', 'c', 'd', 'f']), "Should be: e")
    print(find_missing_letter(['O', 'Q', 'R', 'S']), "Should be: P")
