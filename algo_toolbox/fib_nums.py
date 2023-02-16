# created on: 23:43 16 Feb 2023
# Developed by: Basliel B. Gugsa

def fib_nums(n):
    """
    A function that takes in an integer n and returns the nth fibannaci number

    Parameters
    ----------
    n: int
       The nth fibonnaci number is to be calculated

    Return
    ---------
    fib_sum: int
        The fibonnaci sum to the nth number
    """
    if n <= 1:
        return n
    
    return fib_nums(n-2) + fib_nums(n-1)


if __name__ == '__main__':
    n = int(input())
    print(fib_nums(n))

