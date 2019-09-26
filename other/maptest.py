def map_base_function(x: int) -> int:
    return x * x


result = map(map_base_function, [1, 2, 3, 5, 7, 12])
for i in result:
    print(i, end=',')
# print(map_base_function(12))
