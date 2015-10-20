__author__ = 'sylwia'

FIRST_TEN = ["", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"
SPACE = ' '


def checkio(number):
    len_number = len(str(number))
    hundreds = number / 100 if len_number == 3 else 0
    teens = number % 100 if len_number >= 2 else 0
    units = teens % 10 if 1 < len_number else number
    result = ''
    result += FIRST_TEN[hundreds] + SPACE + HUNDRED + SPACE if hundreds != 0 else ''
    result += SECOND_TEN[units] + SPACE if 10 <= teens <= 19 else ''
    result += OTHER_TENS[teens / 10] + SPACE + FIRST_TEN[units] + SPACE \
        if 20 <= teens <= 99 and units > 0 else OTHER_TENS[teens / 10]
    result += FIRST_TEN[units] + SPACE if teens < 10 else ''

    print result.lstrip().rstrip()
    return result.lstrip().rstrip()


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert checkio(999) == 'nine hundred ninety nine', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
