import re

if __name__ == '__main__':
    consonants = 'qwrtypsdfghjklzxcvbnm'
    vowels = 'aeiou'
    result = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])', input(), flags=re.I)
    if result:
        for line in result:
            print(line)
    else:
        print(-1)
