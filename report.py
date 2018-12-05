from collections import namedtuple

Result = namedtuple("Result", "count average")

a=Result(3, 43.4)
#a.average
#a.count

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count +=1
        average = total/count
    return Result(count, average)

def grouper(results, key):
    while True:
        results[key] = yield from averager()

data = {
    "a;1":  [43, 545, 65, 65, 654],
    "a;2":  [43, 654, 654, 645, 654],
    "b;1": [12, 10, 43, 5, 65, 65, 54],
    "b;2": [34, 21, 21, 43, 54, 54, 65, 54],
}


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(";")
        print("{:2} {:5} averaging {:.2f}{}"
              .format(result.count, group, result.average, unit))

def main(data_param):
    results={}
    for key, values in data_param.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)

    report(results)


main(data)