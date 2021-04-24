def smallest_greater(seq, value):
    difference = max(seq);
    output = value
    for element in seq:
        if element> value:
            if element-value < difference:
                output = element
                difference = element-value
    return output


def greatest_smaller(seq, value):
    difference = max(seq);
    output = value
    for element in seq:
        if element< value:
            if value-element < difference:
                output = element
                difference = value-element
    return output




print(smallest_greater([13, -3, 22, 14, 2, 18, 17, 6, 9], 4))
print(greatest_smaller([13, -3, 22, 14, 2, 18, 17, 6, 9], 4))
print(smallest_greater([1, 2, 9, 5, 3, 10, 9, 4], 9.5))
print(greatest_smaller([1, 2, 9, 5, 3, 10, 9, 4], 9.5))
print(smallest_greater([1, 2, 3, 4], 2.5))
print(greatest_smaller([1, 2, 3, 4], 3.5))