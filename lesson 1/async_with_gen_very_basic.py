from time import sleep
queue = []

def counter():
    counter = 0
    while True:
        counter+= 1
        print(counter)
        yield
    

def printer():
    counter = 0
    while True:
        if counter%3 == 0:
            print('Bang!')
        counter +=1
        yield


def main():
    while True:
        g = queue.pop(0)
        next(g)
        queue.append(g)
        sleep(0.5)


if __name__ =='__main__':
    p1 = counter()
    queue.append(p1)
    p2 = counter()
    queue.append(p2)
    
    main()