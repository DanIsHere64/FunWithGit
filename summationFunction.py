def summation(start, stop, expression):
    return sum(expression(i) for i in range(start, stop + 1))
 summation(1, 10, lambda a : 1)
