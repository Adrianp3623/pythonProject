def sum_odd_digits(number):
    dsum = 0
    # only count odd digits
    while number != 0:     # change this line
        # add the last digit to the sum
        digit = number % 10
        if digit % 2 != 0: # change this line
            # print(digit)
            dsum = dsum + digit # change this line , move
        else:
            dsum  =dsum
            # print("nottt %5d"% (digit))
        # divide by 10 (rounded down) to remove the last digit
        number = number // 10
    return dsum


def sum_even_digits(number):
    m = 1 # the position of the next digit
    dsum = 0 # the sum
    while number // (10 ** (m-1) ) != 0:
        # print("test")
        # get the m:th digit
        digit = (number % (10 ** m)) // (10 ** (m - 1))
        # only add it if even:
        if digit % 2 == 0:
            # print("test %5d"% (digit))
            dsum = dsum + digit
        m = m + 1
    return dsum



print(sum_odd_digits(12345))
# print(sum_odd_digits(123456))

print(sum_odd_digits(456789))

print("done first func test")
print(sum_even_digits(12345))
print(sum_even_digits(456789))