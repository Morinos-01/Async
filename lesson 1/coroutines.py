from inspect import getgeneratorstate

# def subjen():
#     x = 'ready to accept message'
#     message = yield x
#     print(f'subjen received: {message}')

# g = subjen()
# print(getgeneratorstate(g))
# m = g.send(None)
# print(getgeneratorstate(g))

# try:
#     g.send('Ok')
# except StopIteration:
#     print(getgeneratorstate(g))

# print(m)

class blablaexception(Exception):
    pass


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return inner

@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done!')
            break
        except blablaexception:
            print('....................')
            break
        else:
            count += 1
            summ += x
            average = round(summ/count, 2)
    return average

g = average()
g.send(2)
m = g.send(4)
#print(m)

try:
    g.throw(StopIteration)
except StopIteration as e:
    print(f'Average: {e.value}')

