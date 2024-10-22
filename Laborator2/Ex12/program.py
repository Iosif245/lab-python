def group_by_rhyme(words):
    rhyme_groups = {}

    for word in words:
        rhyme_key = word[-2:]
        if rhyme_key in rhyme_groups:
            rhyme_groups[rhyme_key].append(word)
        else:
            rhyme_groups[rhyme_key] = [word]
    return list(rhyme_groups.values())

input_words = ['ana', 'banana', 'carte', 'arme', 'parte']
result = group_by_rhyme(input_words)
print(result)
