"""
模块描述文档

"""


# 指定数量的装饰器函数
def my_func(func):
    """

    :param func:
    :return:
    """
    def func_inner(name: str, age: int, *args, **kwargs) -> int:
        age = age + 10
        # print(name, age)
        return func(name, age, )
    return func_inner


@my_func
def my_test(name, age, *args, **kwargs):
    print(name, age)


if __name__ == '__main__':
    my_test(name='wwfyde', age=18,gender='nv')
