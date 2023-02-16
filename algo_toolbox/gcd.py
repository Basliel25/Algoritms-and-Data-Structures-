# Created on: 00:25 Feb 17 2023
# Author: Basliel B. Gugsa

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(gcd(a, b))
