def to_pig_latin(word):
    #TODO: implement this function
    vowels="aeiouAEIOU"
    # print(word.split())
    if (word[0] in vowels):
        # vowel
        return word+"yay"

    else:
        #  consonant
        if(word[0].isnumeric()):
            return word
        for i in range(len(word)):
            if (word[i] in vowels):
                return word[i:len(word)]+word[0:i]+"ay"









print(to_pig_latin('dog'))
print(to_pig_latin('scratch'))
print(to_pig_latin('is'))
print(to_pig_latin('apple'))
print(to_pig_latin('1287643'))