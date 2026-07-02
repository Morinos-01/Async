def my_decorator(func):
    def inner(*args, **kwargs):
        print('start')
        msg = func(*args, **kwargs)
        print('end')
        return msg
    return inner


@my_decorator
def func_1(a):
    print(f'hello {a}')


func_1(5)
