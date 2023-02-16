# created on: 11:56 11/02/23
# Developed by: Basliel B. Gugsa
def max_product(arr):
    p1 = max(arr)
    arr.remove(p1)
    p2 = max(arr)
    arr.remove(p2)
    return p1*p2


if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    result = max_product(numbers)
    print(result)


