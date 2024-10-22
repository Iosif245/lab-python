def calc_n_numbers_in_fibonacci(n):
    fib_sequence = []

    for i in range(n):
        if i == 0:
            fib_sequence.append(0)
        elif i == 1:
            fib_sequence.append(1)
        else:
            next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_fib)

    return fib_sequence

number_of_elements = input("Enter the number of elements in the Fibonacci sequence: ")
for i in calc_n_numbers_in_fibonacci(int(number_of_elements)):
    print(i, end=" ")