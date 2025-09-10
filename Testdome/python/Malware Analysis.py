def simulate(entries, s):
    """
    :param entries: (list(int)) The numerical record files
    :returns: (list(int)) The record files after running the malware
    """
    start = [-1] * s
    end = [-1] * s

    return [*start, *entries[s:-s], *end]


records = [4, 1, 3, 5, 4, 7, 9]
print(simulate(records, 3))

records = [7, 6, 9, 1, 8, 3, 2]
print(simulate(records, 2))
