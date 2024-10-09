def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def find_gcd(numbers):
    result = numbers[0]
    for i in range(1,len(numbers)):
        result = gcd(result, numbers[i])
    return result

input_numbers = [int(x) for x in input().split()]

print(find_gcd(input_numbers))
