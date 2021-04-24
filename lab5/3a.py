def count_capitals(string):
    count = 0
    for i in string:
        if 65<=ord(i)<=90:
            count+=1

    return count






print(count_capitals("The quick brown fox jumps over the lazy dog"))
print(count_capitals("COMP1730"))
print(count_capitals("qwerty"))
print(count_capitals("coPYrIGht iN thESE LEcTuRes iS EiTHeR OWEned BY tHe aNu Or A tHiRd ParTY WhO hAS LiScEnCEd THe anU TO uSE IT."))