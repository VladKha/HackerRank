def count_substring(s, sub_s):
    counter = 0
    for i in range(len(s)):
        if s[i:i+len(sub_s)] == sub_s:
            counter += 1
    return counter
