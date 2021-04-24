def any_one_is_sum(a,b,c):
    if b + c == a:
        return True
    elif a + b == c:
        return True
    elif c + a == b:
        return True
    else:
        return False
