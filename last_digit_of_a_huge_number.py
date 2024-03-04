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
        base = int((str(lst[0]))[-1])
        exponent = (lst[1] % len(power_endings[base])) - 1
        return power_endings[base][exponent]
    for num in range(len(lst)):
        lst[num] = int((str(lst[num]))[-1])
    while len(lst) != 1:
        new_lst = lst[:-2]
        new_lst.append(last_digit(lst[-2:]))
        lst = new_lst.copy()
    return int((str(lst[0]))[-1])


for n in range(100):
    print(int(str(6**n)[-2:]))
