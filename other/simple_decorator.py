# 这种方式, 没有实现闭包, 虽然有装饰器的形式, 但是却无法完成特定功能
def wrapper(func):
    print('decorator contents')

    return func


@wrapper  # 调用装饰器函数时, 应该会形成一个闭包(理解为闭包函数)才有意义
def my_func(a=1, b=2, c=3):
    print(f'result is :{a + b + c}')


# my_func = wrapper(my_func)

if __name__ == '__main__':
    my_func(2, 3, 6)
    my_func(3, 3, 7)
