__author__ = 'sylwia'


def checkio(text):

    prop_text = text.lower()
    letters_dict = {}
    for t in prop_text:
        if letters_dict.has_key(t):
            letters_dict[t] += 1
        else:
            letters_dict[t] = 1

    dict_alph_key_sort = sorted(letters_dict)
    dict_uniq_values_sort = sorted(dict(zip(letters_dict.values(), letters_dict.keys())).keys(), reverse=True)

    for value in dict_uniq_values_sort:
        for key in dict_alph_key_sort:
            if ord(key) in range(97, 123) and letters_dict[key] == value:
                return key
    return 0


print checkio("Hello World!")
assert checkio("Hello World!") == "l", "Hello test"
assert checkio("How do you do?") == "o", "O is most wanted"
print checkio("One")
assert checkio("One") == "e", "All letter only once."
assert checkio(u"Oops!") == "o", "Don't forget about lower case."
assert checkio(u"AAaooo!!!!") == "a", "Only letters."
assert checkio(u"abe") == "a", "The First."
print("Start the long test")
assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
print("The local tests are done.")

print checkio("Hello World!")
print checkio("How do you do?")
print checkio("fsbd")
