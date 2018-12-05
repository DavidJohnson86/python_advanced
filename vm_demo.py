a=1
def my_max(b):
    c=a
    if c<b:
        return b
    else:
        return c

code_str="""def my_max(b):
    global a
    if a<b:
        return b
    else:
        return a
"""
import parser
from pprint import pprint
st=parser.suite(code_str)
pprint(parser.st2list(st, line_info=True))

import ast
tree=ast.parse(code_str, mode="exec")
pprint(ast.dump(tree))

import dis
print(dis.dis(my_max))