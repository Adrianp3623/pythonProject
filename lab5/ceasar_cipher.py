## a)
def ceasar_shift(string, shift):
    output = ""
    shift_value = shift%26
    for i in string:
        if(i.isalpha()):
            if (65<=ord(i)<=90):
                # upper case
                if ord(i)+shift_value>90:
                    shifted_char = chr(ord(i)+shift_value-26)
                else:
                    shifted_char = chr(ord(i) + shift_value)
                i = i
            elif (97<=ord(i)<=122):
                # lower case
                if ord(i)+shift_value>122:
                    shifted_char = chr(ord(i)+shift_value-26)
                else:
                    shifted_char = chr(ord(i) + shift_value)
            else:
                shifted_char = chr(ord(i)+shift_value)

            output += shifted_char
        else:
            output += i
    return output



## b)
def decrypt_5(code):
    """Prints out the first 5 words decrypted using successively larger shifts
    """
    for i in range(5):
        print(code[i])




def decrypt_search(code):
    """Decrypt the message using increasing shift values whilst searching for 40
    common three letter words. Return the shift value that gives the highest number
    of different three letter words.
    """
    # TODO: implement this function
    pass


def decrypt_find_e(code):
    """Decrypt Ceasar ciphered message by finding most frequently occuring letter
    assume it is an "e" and return the corresponding shift.
    """
    # TODO: implement this function
    pass




## a)
print(ceasar_shift("Et tu, Brutus!", 3))
print(ceasar_shift("IBM", -1))
print(ceasar_shift("COMP1730 is great!", 25))
print(ceasar_shift("COMP1730 is great!", -25))
print(ceasar_shift("uwu", -27))
print(ceasar_shift("You Could Use Facts To Prove Anything That's Even Remotely True.", 29))

## b)
message1 = '''Awnhu pk neoa wjz awnhu pk xaz
              Iwgao w iwj dawhpdu, xqp okyewhhu zawz'''
message2 = '"Jcstghipcsxcv xh iwpi etctigpixcv fjpaxin du zcdlatsvt iwpi vgdlh ugdb iwtdgn, egprixrt, rdckxrixdc, phhtgixdc, tggdg pcs wjbxaxipixdc." (Gjat 7: Jht p rdadc puitg pc xcstetcstci rapjht id xcigdsjrt p axhi du epgixrjapgh, pc peedhxixkt, pc pbeaxuxrpixdc dg pc xaajhigpixkt fjdipixdc. Ugdb Higjcz & Lwxit, "Iwt Tatbtcih du Hinat".)'
message3 = "Cywo cmsoxdscdc gybu cy rkbn drobo sc xy dswo vopd pyb cobsyec drsxusxq. (kddbsledon dy Pbkxmsc Mbsmu)"
print(decrypt_search(message1))
print(decrypt_search(message2))
print(decrypt_search(message3))
print(decrypt_find_e(message1))
print(decrypt_find_e(message2))
