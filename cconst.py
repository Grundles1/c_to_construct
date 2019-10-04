#!/Users/Jesse/anaconda/bin/python
from pprint import pprint, pformat
import sys
import os

from src import interpreter

if __name__=="__main__":
	env = interpreter.interp(sys.argv[1])
	print("")
	print("Your header file contains structures that could look like this:")
	for name, struct in env.items():
		print("{}:\n{}\n".format(name, struct.parse(os.urandom(struct.sizeof()))))