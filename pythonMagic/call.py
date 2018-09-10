class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __call__(self, z):
        return self.x + self.y + z

    # >> > p = Point(3, 4)
    # >> > callable(p)  # 使用 callable 判断对象是否能被调用
    # True
    # >> > p(6)  # 传入参数，对实例进行调用，对应 p.__call__(6)
    # 13  #
        # 3+4+6