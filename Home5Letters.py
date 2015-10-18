__author__ = 'sylwia'

def checkio(text):

    prop_text = text.lower()
    letters_dict = {}
    for t in prop_text:
        if letters_dict.has_key(t):
            s = letters_dict[t] + 1
            letters_dict[t] = s
        else:
            letters_dict[t] = 0

    sorted(letters_dict)

    print sorted(letters_dict)
    print sorted(letters_dict.values(), reverse = True)
    #print [value for (letters_dict, letters_dict.) in sorted(numbers.items())]

    print "*******"
    print sorted(letters_dict.iterkeys(), key = lambda x: letters_dict[x], reverse = True)



    return sorted(letters_dict.values(), reverse = True)

print checkio("Hello World!")
print checkio("How do you do?")