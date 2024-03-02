map_to_roman = {0: ['', '', '', ''],
                1: ['I', 'X', 'C', 'M'],
                2: ['II', 'XX', 'CC', 'MM'],
                3: ['III', 'XXX', 'CCC', 'MMM'],
                4: ['IV', 'XL', 'CD'],
                5: ['V', 'L', 'D'],
                6: ['VI', 'LX', 'DC'],
                7: ['VII', 'LXX', 'DCC'],
                8: ['VIII', 'LXXX', 'DCCC'],
                9: ['IX', 'XC', 'CM']}


def to_roman(val: int) -> str:
    reversed_roman = ''
    digits = [int(x) for x in str(val)]
    for n in range(1, len(digits) + 1):
        reversed_roman += map_to_roman[digits[-n]][n-1][::-1]
    return reversed_roman[::-1]


def from_roman(val: str) -> int:
    pass


print(to_roman(2345))
