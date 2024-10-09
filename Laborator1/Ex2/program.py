def calculate_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for char in string:
        if char in vowels:
            cnt += 1
    return cnt

input_string = input()

print(calculate_vowels(input_string))