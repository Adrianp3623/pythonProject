def count_repetitions(string, substring):
    '''
    Count the number of repetitions of substring in string. Both
    arguments must be strings.
    '''
    n_rep = 0
    # p is the next position in the string where the substring starts
    p = string.find(substring)
    # str.find returns -1 if the substring is not found
    while p !=-1:
        n_rep = n_rep + 1
        # find next position where the substring starts
        string = string[0:p]+string[p + len(substring):]
        # print(p)
        # print(string[0:p]+string[p + len(substring):])

        p = string.find(substring)



    return n_rep



print(count_repetitions('aabsabs', 'abs'))
print(count_repetitions('absabsabs', 'abs'))