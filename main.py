from functools import reduce


def process_numbers(numbers):
    is_positive = lambda x: x > 0
    is_even = lambda x: x%2 == 0
    square = lambda x: x*x
    accumulate = lambda a, b: a+b

    numbers = filter(is_positive, numbers)
    numbers = filter(is_even, numbers)
    numbers = map(square, numbers)
    numbers = reduce(accumulate, numbers)
    
    return numbers
    
    # return reduce(lambda x,y: x+y,
    #        map(square,
    #        filter(is_positive, 
    #        filter(is_even, numbers)
    # )))

