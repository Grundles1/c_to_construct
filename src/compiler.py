import re

from debug_utils import *

delta = {
	"signed" : {
		"int" : "Int32ub",
		"short" : "Int16ub",
		"char" : "Int8ub",
		"float" : "Float32b",
		"double" : "Float64b",
	},
	"unsigned": {
		"int" : "Int32sb",
		"short" : "Int16sb",
		"char" : "Int8sb",
		"float" : "Float32b",
		"double" : "Float64b",
	}
}

def compile_struct(**fields):
	ret = []
	for k, v in fields.items():
		log("Compiling: {}".format((k,v)))
		ret += ['"{}" / {}'.format(k,v)]
	ret = ",\n".join(ret)
	ret = indent(ret)
	ret = "Struct(\n{}{})".format(INDENT, ret)
	return ret

def compile_blk(blk, env):
	ret = {}
	for b in blk.split(";"):
		clean_b = b.replace("\n", "").replace("\t", "")
		log("Block: {}".format(clean_b))

		if re.match("(int|short|char|float|double) (.*)", clean_b):
			sign = None
			groups = re.match("(int|short|char|float|double)\s+(.*)", clean_b).groups()
			
			if len(groups) == 3: sign, typ, name = groups
			elif len(groups) == 2: typ, name = groups
			else: raise Exception("Unrecognized token: {}".format(clean_b))

			if sign: ret[name] = delta[sign][typ]
			else: ret[name] = delta["signed"][typ] 
	
		elif re.match("(\w+)\s+(\w+)", clean_b):
			obj = re.match("(\w+)\s+(\w+)", clean_b)
			typ, name = obj.groups()
			if typ in env: ret[name] = typ
			else: raise Exception("Unrecognized user type: {}".format(clean_b, typ, name, env))
			log("User type: {}".format((typ, name)))

	log("Returning block: {}".format(pformat(ret)))
	return compile_struct(**ret)


def compile_typdef(stack):
	if len(stack) != 2: raise Exception("Stack is not as expected: {}".format(stack))
	ret = None
	typdef, struct = stack

	clean_typdef = typdef.replace("\n","")
	log("typedef, struct: {}".format((clean_typdef, struct)))

	if re.match("typedef.*struct\s+(\w+)\s*", clean_typdef):
		name = re.match("typedef.*struct\s+(\w+)\s*", clean_typdef).group(1)
		ret = { name : indent(struct) }

	else:
		log("Typedef not recognized: {}".format(stack))
	log("Returning typedef: {}".format(ret))
	return ret


def compile(hdr):
	stack = [""]
	frame = 0
	env = {}
	with open(hdr) as f:
		for c in f.read():
			if c == "{":
				if (len(stack) - 1) == frame:
					stack += [""]
					frame += 1
					continue

			elif c == "}":
				if frame == -1: raise Exception("Stack frame has gone negative, did you have too many closing braces?")

				ret_blk = compile_blk(stack[frame], env)
				log("Received blk: {}".format(ret_blk))
				stack[frame] = ret_blk
				frame -= 1
				continue

			elif frame == 0 and c == ";":
				ret_td = compile_typdef(stack)
				log("Returned typedef, Global Env: {}".format((ret_td, env)))
				env.update(ret_td)
				stack = [""]
				log("Updated env: {}".format(env))
				continue

			stack[frame] += c
	return env