def func_wrapper(wrapper_name: str, urls):  # 这里的参数是装饰器函数的参数, 只能执行一次
    # print(func_wrapper)
    print('111111')
    gender = 'nv'

    def func_inner(func_s):  # 闭包函数用来传入被装饰的对象, 只能执行一次

        def func_inners(*args, **kwargs):  # 接收被装饰函数传入的参数
            """
            完成额外增加的功能
            :param args:
            :param kwargs:
            :return:
            """
            print(3333)
            print(wrapper_name)
            print(gender, urls)

            return func_s(*args, **kwargs)  # 保证被装饰器函数的内容被执行

        return func_inners

    return func_inner  # 返回闭包函数外层


# func_wrapper(wrapper_name='my')  # 直接调用装饰器,  相当于执行函数和开辟了几个内存空间
@func_wrapper(wrapper_name='my', urls='/')
def func(name, age=19):
    print(4444)
    print(name, age)
    print('检测被装饰函数的执行顺序')
    print('测试该代码是否会被执行')
    return True


# 调用装饰器时, 会执行装饰器函数外层的内容

func('我的内容', 20)
func('我的内容2', 22)
