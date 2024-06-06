from functools import reduce


def process_numbers(numbers):
    square = lambda x: x*x
    is_even = lambda x: x%2 == 0
    is_positive = lambda x: x > 0
    
    return reduce(lambda x,y: x+y,
        map(square,
            filter(is_positive, 
                filter(is_even, numbers)
            )
        )
    )
    


init_numbers = range(10)
test_numbers = [1, 2, 3, 4, 5, -2, -4]
print(process_numbers(test_numbers))

# 0, 2, 4, 6, 8
# 0, 4, 16, 36, 64
#     20  +  100
#        120

