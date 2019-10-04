## C to Construct interpreter and compiler

# interpreter

This is a compiler between C typedefs and and Python Construct library structs.  Given a header file, it can be interpreteted to produce a python dictionary from name of structs to Construct structs.  Running this interpreter directly will cause the program to attempt to analyze the structs in the header and then print out what a random structure (all fields are randomly generated) would look like
  
`python cconst.py test.h`  or `./cconst.py test.h` (if you make the exe executable)  
  
or by using it's API:  
  
```
import cconst
  
test_structs = cconst.inter("test.h")

bitstream = ...

my_ints = test_structs["my_int"].parse(bitsteam)

my_ints.a
```

# compiler

The compiler works much like the interpreter but instead prints a python file containing the source code you would need to write in order to implement the header file structs in construct i.e.  
  
```
./cconstc.py test.h
```
  
will yield:  
  
```
# The python file for construct objects, compiled from test.h
# Compiled at 2019-10-03T23:08:12.125523
# Compiled by Jesse

from construct import *

my_int_t = Struct(
    "a" / Float64b,
    "c" / Int32ub,
    "b" / Float32b,
    "d" / Int32ub,
    "y" / Int8ub,
    "x" / Int32ub,
    "z" / Int16ub
  )

my_other_int_t = Struct(
    "a" / Float64b,
    "c" / Int32ub,
    "b" / Float32b,
    "d" / Int32ub,
    "my_int" / Struct(
        "a" / Float64b,
        "c" / Int32ub,
        "b" / Float32b,
        "d" / Int32ub,
        "y" / Int8ub,
        "x" / Int32ub,
        "z" / Int16ub
      ),
    "y" / Int8ub,
    "x" / Int32ub,
    "z" / Int16ub
  )
```