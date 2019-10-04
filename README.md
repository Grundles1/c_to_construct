## C to Construct compiler

This is a compiler between C typedefs and and Python Construct library structs.  Given a header file, it can be parsed by either calling the main exe `parse.py` on a header:  
  
`python parse.py test.h`  or `./parse.py test.h` (if you make the main exe executable)  
  
or by using it's API:  
  
```
import parse
  
my_dict_of_parsers = parse.parse("<header file path>")

bitstream = ...

obj_vals = my_dict_of_parsers["<my structure from header>"].parse(bitsteam)

obj_vals.my_field
```

