#python2 def next
#python3 def __next__

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):  # 返回迭代器对象本身
        return self

    def __next__(self):      # 返回容器下一个元素
        self.a, self.b = self.b, self.a + self.b
        return self.a


a =Fib()
for i in a:
    print(i)
    if i > 10000:
        break

# >>> fib = Fib()
# >>> for i in fib:
# ...     if i > 10:
# ...         break
# ...     print i
# ...
# 1
# 1
# 2
# 3
# 5
# 8