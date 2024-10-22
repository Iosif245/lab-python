def check_palindrome(number):
    number_clone = number
    reverse_number = 0
    while number > 0:
        remainder = number % 10
        reverse_number = reverse_number * 10 + remainder
        number = number // 10
    if number_clone == reverse_number:
        return True
    else:
        return False


def palindrome_info(numbers):
    palindromes = [num for num in numbers if check_palindrome(num)]

    if palindromes:
        return len(palindromes), max(palindromes)
    else:
        return 0, None

input_numbers = [121, 131, 123, 454, 678, 99, 11]
result = palindrome_info(input_numbers)
print(result)
