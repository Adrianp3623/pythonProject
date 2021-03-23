def median(a:int,b:int,c:int) -> int:
    if (a>b):
        temp = a
        a= b
        b = temp
        if (b>c):
            temp1 = b
            b = c
            c = temp1
    else:
        if (b>c):
            temp1 = b
            b = c
            c = temp1
    return b

print(median(1,2,3))
print(median(1,3,2))
print(median(2,1,3))
print(median(2,1,2))
print(median(1,1,1))


