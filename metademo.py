import collections

class OrderedClass(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        return collections.OrderedDict()

    def __new__(cls, name, bases, namespace, **kwargs):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        return result

class A(metaclass=OrderedClass):
    def one(self):
        pass

    def two(self):
        pass

a=A()