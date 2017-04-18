if __name__ == '__main__':
    s = input()
    vowels = 'aeiouy'
    is_beautiful = True
    for i in range(len(s)-1):
        if s[i] == s[i+1] or (s[i] in vowels and s[i+1] in vowels):
            is_beautiful = False
            break
    print('Yes' if is_beautiful else 'No')
