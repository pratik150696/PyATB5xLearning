dict1 = {"a": 1, "b": 2, "c":3}
dict2 = {"a": 1, "b": 2}

missing_key = set(dict1.keys())-set(dict2.keys())
print(missing_key)