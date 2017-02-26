def capitalize(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
