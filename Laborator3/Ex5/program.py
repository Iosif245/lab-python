def validate_dict(rules, d):
    for key, prefix, middle, suffix in rules:
        if key not in d:
            return False
        value = d[key]

        if not value.startswith(prefix):
            return False
        if middle not in value[1:-1]:
            return False
        if not value.endswith(suffix):
            return False

    for key in d:
        if key not in {rule[0] for rule in rules}:
            return False

    return True

input_rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
input_d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
print(validate_dict(input_rules, input_d))
