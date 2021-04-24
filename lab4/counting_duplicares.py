def count_duplicates(seq):
    count = 0
    counts = dict()
    for i in seq:
        counts[i] = counts.get(i,0)+1
    # print(counts)
    for j in counts.values():
        if j >1:
            count+=j-1
        # print(j)
    return count



print(count_duplicates([-1, 2, 4, 2, 0, 4]))
print(count_duplicates("Immaterium"))
print(count_duplicates([1, 2, 3, 4]))
print(count_duplicates((1, 2, 3, 3, 3, 4, 1)))