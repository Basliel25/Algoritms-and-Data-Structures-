# Created on: 00:17 17th Feb 2023
# Author: Basliel B. Gugsa

def fibonnaci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonnaci_last_digit(n))
