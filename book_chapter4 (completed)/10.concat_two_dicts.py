dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

result = {k: {dict1[k], dict2[k]} for k in dict1.keys() & dict2.keys()}

print(result)