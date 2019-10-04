from parse import parse
from pprint import pprint
import os

ret = parse("test.h")
print("")
print("")

print("Received following from parsing \"test.h\":")
print("")
pprint(ret)

a = ret["my_int"]
print("my_int from ret of parse:")
pprint(a)

rand_a_bits = os.urandom(a.sizeof())
print("Random bits the length of my_int:")
print(repr(rand_a_bits))


print("Using a to parse the random string")
parsed_a = a.parse(rand_a_bits)
print(parsed_a)