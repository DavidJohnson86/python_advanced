class NamedVector:
    """ a .... x, y, z """
    def __init__(self):
        self.__data=[]
        while len(self.__data)<ord('z')-ord('a'):
            self.__data.append(0)

    def __setattr__(self, key, value):
        if isinstance(key, str) and len(key)==1:
            if key >= 'a' and key <= 'z':
                pos=ord(key)-ord('a')
                self.__data[pos]=value
        else:
            super().__setattr__(key, value)

    def __getattr__(self, key):
        if isinstance(key, str) and len(key)==1:
            if key >= 'a' and key <= 'z':
                pos=ord(key)-ord('a')
                self.__data[pos]
        else:
            super().__setattr__(key)

n=NamedVector()
n.a=4
n.b=7
n.x=23
print(n._NamedVector__data)