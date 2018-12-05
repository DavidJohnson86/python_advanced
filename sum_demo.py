from time import sleep
from inspect import getgeneratorstate

def avg_cor():
    sum=0
    count=0
    in_d=0
    while in_d is not None:
        in_d=yield (sum/count if count != 0 else 0)
        if in_d is None:
            break
        sum+=in_d
        print(getgeneratorstate(avg))
        count+=1
    return sum/count

avg=avg_cor()
next(avg)
for i in [32,343, 54, 54, 65, 76]:
    avg.send(i)
try:
    avg.send(None)
except StopIteration as res:
    print("Avg is "+str(res.value))

#------------------------------------------------------

def give10():
    for i in range(10):
        yield i

def chain(*iterables):
    for e in iterables:
        yield from e
        #kb. valami ilyesmi: while e is not StopIterion: next(e)

a=[3, 5, 6, 8]
b=[10, 12, 15]

c=chain(give10(), give10())
for e in c:
    print(e)