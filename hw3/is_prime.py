# COMP1730/6730 S1 2021 - Homework 3
# Submission is due 9:00am, Monday the 29th of March, 2021.

# YOUR ANU ID: u7274552
# YOUR NAME:Junhao Wang

import math



def is_factor(a, b):
    if (a%b == 0):
        return True
    return False


def is_prime(n):
    for i in range(2,n):
        if is_factor(n,i):
            return False
    return True


def count_prime_factors(n):
    count = 0
    for i in range(2,n+1):
        if ((is_prime(i)) and (is_factor(n,i)) ):
            count= count+1
    return count

# REMEMBER THAT THIS FILE (WHEN YOU SUBMIT IT) MUST NOT CONTAIN ANYTHING
# OTHER THAN YOUR FUNCTION DEFINITIONS AND COMMENTS.
# YOU MAY NOT IMPORT ANY MODULES OTHER THAN THE 'math' MODULE
