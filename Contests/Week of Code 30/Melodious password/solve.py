def choose_letter(letters1, letters2, length):
    if length == 0:
        yield ''
    else:
        for letter in letters1:
            for word in choose_letter(letters2, letters1, length-1):
                yield (letter + word)


if __name__ == '__main__':
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxz'

    n = int(input())

    for word in choose_letter(vowels, consonants, n):
        print(word)

    for word in choose_letter(consonants, vowels, n):
        print(word)
