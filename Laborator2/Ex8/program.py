def divisibility_by_ascii(x = 1, lists = None, flag = True):
    if lists is None:
        lists = []
    generated_result = []
    for string in lists:
        generated_result_sublist = []
        for ch in string:
            if flag:
                if ord(ch) % x == 0:
                    generated_result_sublist.append(ch)
            else:
                if ord(ch) % x != 0:
                    generated_result_sublist.append(ch)
        if len(generated_result_sublist) > 0:
            generated_result.append(generated_result_sublist)

    return generated_result

print(divisibility_by_ascii(x = 2, lists = ["test", "hello", "lab002"], flag = False ))