def count_words(text):
    words = text.split()
    return len(words)

input_text = input()

print(count_words(input_text))