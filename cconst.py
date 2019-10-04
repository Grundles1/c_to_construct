#!/Users/Jesse/anaconda/bin/python
from pprint import pprint, pformat
import sys


from src import interpreter, compiler

if __name__=="__main__":
	env = interpreter.interp(sys.argv[1])
	pprint(env)