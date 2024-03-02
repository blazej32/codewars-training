map_to_roman = [['', '', '', ''],
                ['I', 'X', 'C', 'M'],
                ['II', 'XX', 'CC', 'MM'],
                ['III', 'XXX', 'CCC', 'MMM'],
                ['IV', 'XL', 'CD'],
                ['V', 'L', 'D'],
                ['VI', 'LX', 'DC'],
                ['VII', 'LXX', 'DCC'],
                ['VIII', 'LXXX', 'DCCC'],
                ['IX', 'XC', 'CM']]


def to_roman(val: int) -> str:
    reversed_roman = ''
    digits = [int(x) for x in str(val)]
    for n in range(1, len(digits) + 1):
        reversed_roman += map_to_roman[digits[-n]][n-1][::-1]
    return reversed_roman[::-1]


def from_roman(roman_num: str) -> int:
    arabic = [0, 0, 0, 0]
    for row in [4, 9]:
        for num in map_to_roman[row]:
            if num in roman_num and not arabic[map_to_roman[row].index(num)]:
                arabic[map_to_roman[row].index(num)] = row
                roman_num = roman_num.replace(num, '')
    for row in [8, 7, 6, 5, 3, 2, 1]:
        for num in map_to_roman[row]:
            if num in roman_num and not arabic[map_to_roman[row].index(num)]:
                arabic[map_to_roman[row].index(num)] = row
    str_arabic = [str(x) for x in arabic[::-1]]
    return int(''.join(str_arabic).lstrip('0'))



'''
    for num in map_to_roman[4]:
        if num in roman_num:
            arabic[map_to_roman[4].index(num)] = 4
            roman_num.replace(map_to_roman[4].index(num), '')
    for num in map_to_roman[9]:
        if num in roman_num:
            arabic[map_to_roman[9].index(num)] = 9
            roman_num.replace(map_to_roman[9].index(num), '')
'''