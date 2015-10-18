__author__ = 'sylwia'

def checkio(data):

    if len(data) >= 10:
        if any(symbol_digit.isdigit() for symbol_digit in data):
            if any(symbol_up.isupper() for symbol_up in data):
                if any(symbol_low.islower() for symbol_low in data):
                    return True
    return False

# minumum 10 symbols
# min one digit
# min one uppercase
# min one lowercase

print checkio('A1213pokl')
print checkio('bAse730onE4')