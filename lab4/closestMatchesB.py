def smallest_greater(seq, value):
    for element in seq:
        if element>value:
            return element

# method1
# def greatest_smaller(seq, value):
#     for element in reversed(seq):
#         if element<value:
#             return element

# //method2
def greatest_smaller(seq, value):
    for element in seq[::-1]:
        if element<value:
            return element



print(smallest_greater([1, 2, 3, 4, 5, 6, 7, 8, 9], 1.5))
print(greatest_smaller([1, 2, 3, 4, 5, 6, 7, 8, 9], 8.5))
print(smallest_greater([1, 3, 4, 7, 9], 5))
print(greatest_smaller([1, 3, 4, 7, 9], 5))