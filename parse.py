#!/Users/Jesse/anaconda/bin/python
from pprint import pprint, pformat

from construct import *
import sys
import re

delta = {
	"signed" : {
		"int" : Int32ub,
		"short" : Int16ub,
		"char" : Int8ub,
		"float" : Float32b,
		"double" : Float64b,
	},
	"unsigned": {
		"int" : Int32sb,
		"short" : Int16sb,
		"char" : Int8sb,
		"float" : Float32b,
		"double" : Float64b,
	}
}
def parse_blk(blk):
	ret = {}
	for b in blk.split(";"):
		clean_b = b.replace("\n", "").replace("\t", "")
		print("Block: {}".format(clean_b))

		if re.match("(int|short|char|float|double) (.*)", clean_b):
			sign = None
			groups = re.match("(int|short|char|float|double)\s+(.*)", clean_b).groups()
			if len(groups) == 3: sign, typ, name = groups
			elif len(groups) == 2: typ, name = groups
			else: raise Exception("Unrecognized token: {}".format(clean_b))

			if sign: ret[name] = delta[sign][typ]
			else: ret[name] = delta["signed"][typ] 
	
		elif re.match("short (.*)", clean_b):
			name = re.match("int (.*)", clean_b).group(1)
			ret[name] = Int32ub 
	print("Returning block: {}".format(pformat(ret)))
	return Struct(**ret)

def parse_typdef(stack):
	if len(stack) != 2: raise Exception("Stack is not as expected: {}".format(stack))
	ret = None
	typdef, struct = stack

	clean_typdef = typdef.replace("\n","")
	print("typedef, struct: {}".format((clean_typdef, struct)))

	if re.match("typedef.*struct\s+(\w+)\s*", clean_typdef):
		name = re.match("typedef.*struct\s+(\w+)\s*", clean_typdef).group(1)
		ret = { name:struct }

	else:
		print("Typedef not recognized: {}".format(stack))
	print("Returning typedef: {}".format(ret))
	return ret

def parse(hdr):
	stack = [""]
	frame = 0
	ret = {}
	with open(hdr) as f:
		for c in f.read():
			if c == "{":
				if (len(stack) - 1) == frame:
					stack += [""]
					frame += 1
					continue
			elif c == "}":
				if frame == -1: raise Exception("Stack frame has gone negative, did you have too many closing braces?")

				ret_blk = parse_blk(stack[frame])
				print("Received blk: {}".format(ret_blk))
				stack[frame] = ret_blk
				frame -= 1
				continue

			elif frame == 0 and c == ";":
				ret_td = parse_typdef(stack)
				print("Returned typedef, Global Env: {}".format((ret_td, ret)))
				ret.update(ret_td)
				stack = [""]
				print("Updated env: {}".format(ret))
				continue
			stack[frame] += c
	return ret

if __name__=="__main__":
	parsed_prog = parse(sys.argv[1])
	pprint(parsed_prog)