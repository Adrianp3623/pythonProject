import math


canberra_population = 196037
canberra_families = 50352

# TODO: Calculate this figure
canberra_singless = 7243
canberra_couple = 22850
canberra_without_children = canberra_families - canberra_singless - canberra_couple

children_per_family = 1.8

canberra_singles = canberra_population - canberra_couple * (2 + children_per_family) - canberra_singless * (
            1 + children_per_family) \
                - canberra_without_children * 2 + canberra_singless

canberra_singles = math.ceil(canberra_singles)

print("number of single adults:", math.ceil(canberra_singles))
