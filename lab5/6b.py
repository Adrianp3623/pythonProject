def remove_substring_everywhere(string, substring):
    '''
    Remove all occurrences of substring from string, and return
    the resulting string. Both arguments must be strings.
    '''
    p = string.find(substring)
    lsub = len(substring) # length of the substring
    while p >= 0:
        # string[p : len(string) - lsub] = string[p + lsub : len(string)]
        string = string[0:p]+string[p+lsub:len(string)]
        # print("string111: %s"%string)
        p = string.find(substring)
    return string



print(remove_substring_everywhere('abcde', 'bc'))
print(remove_substring_everywhere('absabsabs', 'abs'))
print(remove_substring_everywhere("Reading is good this is good is is good a is good waste is good of is good time is good", " is good"))