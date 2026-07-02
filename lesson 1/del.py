from inspect import getgeneratorstate


class blablaexception(Exception):
    pass


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return inner


def subjen():
    while True:
        try:
            message = yield
        except StopIteration:
            print('really?')
            break
        else: 
            print('........', message)
    return ('thats all!')

@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except blablaexception as e:
    #         g.throw(e)
    message = yield from g
    print(message)
  
g = delegator(subjen())
g.send('OK')
g.throw(StopIteration) 