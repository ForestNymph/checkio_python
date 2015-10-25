__author__ = 'sylwia'


def check_connection(network, first, second):
    search_set, result_set = set(), set()

    search_set.add(first)
    result_set.add(first)

    while search_set:
        first_dron = search_set.pop()
        for pair in network:
            if first_dron in pair:
                second_dron = (pair.replace(first_dron, "")).replace("-", "")
                search_set.add(second_dron) if second_dron not in result_set else 0
                result_set.add(second_dron)

    return True if second in result_set else False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("mr99-dr101", "mr99-out00"),
        "mr99", "dr101") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
