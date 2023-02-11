# created on: 11:56 11/02/23
# Developed by: Basliel B. Gugsa
def max_pairwise_product(numbers):
    n = len(numbers)
    max_index1 = -1
    for i in range(n):
        if max_index1 == -1 or numbers[i] > numbers[max_index1]:
            max_index1 = i
    
    max_index2 = -1
    for i in range(n):
        if i != max_index1 and (max_index2 == -1 or numbers[i] > numbers[max_index2]):
            max_index2 = i

    return numbers[max_index1] * numbers[max_index2]

if __name__ == '__main__':
    numbers = list(map(int, input("Enter a list of integers: ").split()))
    result = max_pairwise_product(numbers)
    print("The maximum piecewise product is:", result)


