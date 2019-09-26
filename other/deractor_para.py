def demo(*args, **kwargs):
    print(*args)
    print(kwargs)


demo(1, 2, 3, 4, a=1, b=2)

my_dict = {'a': 1, 'b': 2}

for i in my_dict.values():
    print(i)
