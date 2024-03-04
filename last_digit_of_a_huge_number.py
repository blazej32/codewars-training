power_endings = [[0],
                 [1],
                 [2, 4, 8, 6],
                 [3, 9, 7, 1],
                 [4, 6],
                 [5],
                 [6],
                 [7, 9, 3, 1],
                 [8, 4, 2, 6],
                 [9, 1]]


def last_digit(lst):
    if len(lst) == 0:
        return 1
    if len(lst) == 2:
        if lst[1] == 0:
            return 1
        return power_endings[lst[0]][(lst[1] % len(power_endings[lst[0]])) - 1]
    while len(lst) != 1:
        new_lst = lst[:-2]
        new_lst.append(last_digit(lst[-2:]))
        lst = lst.copy()
    return lst[0]


print(last_digit([0, 0, 0]))
