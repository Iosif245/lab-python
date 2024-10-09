def count_bits_with_one(number):
    return bin(number).count('1')

input_number = int(input())

print(count_bits_with_one(input_number))