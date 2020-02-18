def find_max(numbers):
    max = numbers[0]#这里的max是bulitin function内建函数 可以renamed 为maximum
    for number in numbers:
        if number > max:
            max = number
    return max

