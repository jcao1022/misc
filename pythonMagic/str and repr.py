class Foo(object):
    def __init__(self, name):
        self.name = name

# >>> print Foo('ethan')
# <__main__.Foo object at 0x10c37aa50>


class Foo(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Foo object (name: %s)' % self.name

# >>> print Foo('ethan')      # 使用 print
# Foo object (name: ethan)
# >>>
# >>> str(Foo('ethan'))       # 使用 str
# 'Foo object (name: ethan)'
# >>>
# >>> Foo('ethan')             # 直接显示
# <__main__.Foo at 0x10c37a490>


class Foo(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Foo object (name: %s)' % self.name
    def __repr__(self):
        return 'Foo object (name: %s)' % self.name

# >>> Foo('ethan')
# 'Foo object (name: ethan)'



class Foo(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Foo object (name: %s)' % self.name
    __repr__ = __str__


