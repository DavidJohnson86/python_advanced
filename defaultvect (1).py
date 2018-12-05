from numbers import Integral
from typing import Sequence
import unittest

class DefaultVector2D:
    def __init__(self, default_val=0):
        self.__data=[] # type: list
        #self.__data:Sequence=[]
        self.__default_val = default_val

    def __getitem__(self, item):
        if isinstance(item, tuple) and len(item)==2:
            x, y = item
            if isinstance(x, Integral) and isinstance(y, Integral):
                if len(self.__data)>x and len(self.__data[x])>y:
                    return self.__data[x][y]
                return 0
                #raise IndexError("{}, {} are larger than the exisiting indexes".format(x, y))
            #egyéb variációl
            return 0

    def __setitem__(self, item, value):
        if isinstance(item, tuple) and len(item)==2:
            x, y = item
            if isinstance(x, Integral) and isinstance(y, Integral):
                while len(self.__data) <= x:
                    self.__data.append([])
                while len(self.__data[x]) <= y:
                    self.__data[x].append(self.__default_val)
                self.__data[x][y]=value
                return
        raise ValueError("")

    def __len__(self):
        return len(self.__data)

    def size(self):
        sizes=[]
        for row in self.__data:
            sizes.append(len(row))
        return sizes

    def __str__(self):
        res="DefaultVector2D:\n"
        for row in self.__data:
            res+=str(row)+"\n"
        return res

v=DefaultVector2D()
v[2, 3]=5
print(v)
print(v.size())

class DefVect2DTest(unittest.TestCase):
    def test_init(self):
        v=DefaultVector2D()
        self.assertEqual(0, len(v))

    def test_vect(self):
        v=DefaultVector2D()
        v[2,3]=9
        v[3,5]=42
        self.assertEqual((0,0,0,9), v[2])
        self.assertEqual([(0,0,0,9), (0,0,0,0,0,42)], v[2:4])