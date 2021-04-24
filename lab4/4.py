def find_element(sequence, element):
    i = 0
    while (sequence[i] != element and i<len(sequence)) :
            if i == len(sequence)-1 :
                i= i+1
                break
            i = i + 1

    return i

#
# def find_element(sequence, element):
#     i = 0
#     while sequence[i] != element:
#         if i < len(sequence):
#            i = i + 1
#         i = i + 1
#     return i



print(find_element([1, 2, 3], 1))
print(find_element([1, 2, 3], 2))
print(find_element([-2, 3, 4, -5], -5))
print(find_element([1, 2, 3], 4))