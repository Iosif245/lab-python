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

number_to_check = input()

print(check_palindrome(int(number_to_check)))