def any_one_is_sum(a,b,c):
    sum_c=a+b
    sum_b=a+c
    sum_a=b+c
    if ((sum_c == c) or (sum_b == b) or (sum_a == a) ):
        return True
    else:
        return False