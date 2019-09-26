def function_out(func):
    print('执行顺序', '装饰器函数内容')

    def function_in(*args, **kwargs):
        print('正在进行验证 ... ')

        print('正在进行验证 ...', args, kwargs)
        func(*args, **kwargs)  # 装饰器最后再执行

    return function_in
# function_out(login)(a)
# 为函数添加装饰器
@function_out
def login(*args, **kwargs):
    print('--开始登录--,被装饰函数, a = ', args, kwargs)


login(10, 20, c=100)
