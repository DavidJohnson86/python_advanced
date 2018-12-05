class SingletonDemo:
    _singleton = None
    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = object.__new__(cls)
            #, *args, **kwargs)
        return cls._singleton

    def __init__(self, val):
        self.val=val

    def __str__(self):
        return str(self.val)

a=SingletonDemo(3)
b=SingletonDemo(5)
print(a, b, a is b)