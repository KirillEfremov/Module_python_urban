data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
s = 0
def summ():
    for i in data_structure:
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, dict) or isinstance(i, str) or isinstance(i, set):
            s = summ()
        if isinstance(i, int):
            s += i
    return s
