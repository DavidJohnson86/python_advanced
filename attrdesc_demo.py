class Quantity:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError("value must be greater than 0")


class DemoItem:
    weight = Quantity("weight")

    def __init__(self, w):
        self.weight=w

a=DemoItem(2)
b=DemoItem(-2)