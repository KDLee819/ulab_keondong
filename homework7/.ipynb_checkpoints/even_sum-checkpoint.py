# Most important: Name of the file at the top
# File: even_sum.py

# Call import statements at the top
import numpy as np

def sum_even_numbers(numbers):
    """
    Returns the sum of all even numbers
    in a given list or array.
    Inputs:
    Outputs:
    """

    sum = np.sum(num for num in numbers if num % 2 == 0)
    return sum

## This should be in my hw submission repository!