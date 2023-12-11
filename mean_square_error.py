def solution(array_a, array_b):
    squares_of_differences = 0
    for index in range(0, len(array_a)):
        squares_of_differences += ((abs(array_a[index] - array_b[index])) ** 2)
    average = squares_of_differences / len(array_a)
    return average
