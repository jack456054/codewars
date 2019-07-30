def spin_words(sentence):
    words_list = sentence.split()
    for index, word in enumerate(words_list):
        if len(word) >= 5:
            words_list[index] = ''.join(list(reversed(words_list[index])))
    return ' '.join(words_list)


if __name__ == '__main__':
    print(spin_words("I an so handsome"))
