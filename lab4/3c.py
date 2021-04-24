def most_average(numbers):
    average =    sum(numbers) / len(numbers)
    closest = max(numbers); #initialise dw
    result = 0;
    for number in numbers:
        if abs(average-number)<closest:
            closest =abs(average-number)
            result = number
    return result







print(most_average([1, 2, 3, 4]))
print(most_average([-1, 3, -8, 1]))
print(most_average([-3.3, 8.2, 0, -9, 9]))