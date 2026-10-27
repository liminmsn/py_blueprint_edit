# F:\python\one\test\ts.py
from pytsast import factory as ts

node = ts.createIdentifier("hello")
print(node.serialize().model_dump_json(indent=2))