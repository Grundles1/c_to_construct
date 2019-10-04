#!/Users/Jesse/anaconda/bin/python
from pprint import pprint, pformat

from src import interpreter, compiler

if __name__=="__main__":
	env = parse(sys.argv[1])
	pprint(env)