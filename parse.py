from pprint import pprint

def parse(hdr):
	stack = [""]
	frame = 0
	with open(hdr) as f:
		for c in f.read():
			if c == "{":
				if len(stack) == frame:
					stack += [""]
			stack[frame] += c
	return stack

if __name__=="__main__":
	parsed_prog = parse(sys.argv[1])
	pprint(parsed_prog)