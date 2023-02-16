# Created on: 00:37 17 Feb 2023
# Author: Basliel B. Gugsa
def lcm(a , b):
    return a*b

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
