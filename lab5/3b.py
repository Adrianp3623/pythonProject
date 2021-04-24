def count(seq, prop):
    count = 0
    for i in seq:
        if prop(i):
            count+=1
    return count





print(count([1, 2, 3, 4], lambda x: x == 2))
print(count("COMP1730", lambda x: 65 <= ord(x) <= 90))
print(count([3, 1.3, 38, 1, -0.2, -39, 3.14], lambda x: x < 0))
print(count([], lambda x: x > 9))






