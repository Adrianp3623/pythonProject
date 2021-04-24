def count_in_bin(values, lower, upper):
    count = 0
    # method 1
    # for i in values:
    #     if (i>lower and i<= upper):
    #         count+=1
    # method 2
    for i in range(len(values)):
        if (values[i]>lower and values[i]<=upper):
            count+=1
    return count



def histogram(values, dividers):
    # result = []
    # start = 0
    # for i in range(len(dividers)+1):
    #     print(values[start])
    #     print(dividers[i])
    #     # values[values.index(dividers[i])]
    #     print(count_in_bin(values,values[start],values[values.index(dividers[i])]))
    #     result[i] = count_in_bin(values,values[start],values[values.index(dividers[i])])
    #     print(result[i])
    #     start = values.index(dividers[i]) +1
    # return result
    dividers.sort()
    hist = []
    if len(dividers)>=1:
        hist.append(len([1 for i in values if i<dividers[0]]))
        for i in range(1,len(dividers)):
            hist.append(count_in_bin(values,dividers[i-1],dividers[i]))
        hist.append(len([1 for i in values if i > dividers[-1]]))

    return hist

print(count_in_bin([1, 2, 3], 1, 2))
import random
random.seed(19)
rvs = [random.uniform(0, 1) for _ in range(1000)]
print(count_in_bin(rvs, 0.5, 1))
rvs2 = [random.uniform(-5, 9) for _ in range(1000)]

values1 = [1,2,3,4,5,6,7,8,9,10]
dividers1 = [2,5,7]
print(histogram(values1,dividers1))


print(histogram(rvs2, [-3, -1, 0, 1, 9]))
print(sum(histogram(rvs, [0.1, 0.5, 0.8])) == 1000)