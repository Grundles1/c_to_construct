#!/Users/Jesse/anaconda/bin/python
import sys
from datetime import datetime
import os


from src import compiler

if __name__=="__main__":
	python_construct = compiler.compile(sys.argv[1])
	print("# The python file for construct objects, compiled from {}".format(sys.argv[1]))
	print("# Compiled at {}".format(datetime.now().isoformat()))
	print("# Compiled by {}".format(os.environ["USER"]))
	print("")
	print("from construct import *")
	print("")

	for k,v in python_construct.items():
		print("{} = {}".format(k,v))
		print("")