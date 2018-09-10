class Fib1(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
            # print(a)
        return a

# >>> fib = Fib1()
# >>> fib[0], fib[1], fib[2], fib[3], fib[4], fib[5]
# (1, 1, 2, 3, 5, 8)

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, slice):   # 如果 n 是 slice 对象
            a, b = 1, 1
            start, stop = n.start, n.stop
            L = []
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a, b = b, a + b
            return L
        if isinstance(n, int):     # 如果 n 是 int 型
            a, b = 1, 1
            for i in range(n):
                a, b = b, a + b
            return a
# fib = Fib()
# print(fib[0:3])

class P(object):
    def __init__(self):
        self.coordinate = {}

    def __str__(self):
        print("point(%s)" % self.coordinate)

    def __getitem__(self, key):
        print(self.coordinate.get(key))

    def __setitem__(self, key, value):
        self.coordinate[key] = value

    def __delitem__(self, key):
        del self.coordinate[key]
        print('delete %s' % key)

    def __len__(self):
        return len(self.coordinate)

    __repr__ = __str__

p = P()
p['x'] = 2    # 对应于 p.__setitem__('x', 2)
p['y'] = 5    # 对应于 p.__setitem__('y', 5)
p             # 对应于 __repr__
len(p)        # 对应于 p.__len__
p['x']        # 对应于 p.__getitem__('x')
p['y']        # 对应于 p.__getitem__('y')
del p['x']    # 对应于 p.__delitem__('x')
p
len(p)



