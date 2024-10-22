def my_function(*args, **keys):
    count = 0
    for arg in args:
        if arg in keys.values():
            count += 1
    return count

result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)
