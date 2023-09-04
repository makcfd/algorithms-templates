# import time


# def time_it(func: callable):
#     def wrapper(n):
#         start_time = time.time()
#         result = func(n)
#         end_time = time.time()
#         print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
#         return result
#     return wrapper


# @time_it
# def slow_function(n):
#     time.sleep(n)


# print(f"decorated results is: {slow_function(1)}")


# slow_function = time_it(slow_function)
# print(f"func in func result is: {slow_function(1)}")


# change function behaviour
from collections.abc import Callable
from functools import wraps


def amazing(func: Callable):
    @wraps(func)
    def new_sq_func(x: int):
        print("Hello from Amazing decorator")
        return func(x)
    return new_sq_func


@amazing
def square_int_number(x: int) -> int:
    """Simple function that squares int number
    Input:
    x - integer
    Output:
    Squared input value
    """
    return x ** 2


print(square_int_number(2))
print(square_int_number.__doc__)

square_int_number_2 = amazing(square_int_number)

print("another decoration approach: ", square_int_number_2(2))
