
def fibonaci(X: int) -> int:
    """
    This function calculates the nth Fibonacci number using recursion.

    Parameters:
    X (int): The position of the Fibonacci number to be calculated.

    Returns:
    int: The nth Fibonacci number.

    The Fibonacci sequence is a series of numbers where a number is the addition of the two preceding ones, usually starting with 0 and 1.
    """
    if X == 0:
        return 0
    elif X == 1:
        return 1
    else:
        return fibonaci(X-1) + fibonaci(X-2)
