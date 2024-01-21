# The case for the use of variable scopes

# If all variables in a program were global, wouldn't it be easier? It depends.
# It might be easier for simple programs. However, variable scope exists to
# solve a problem: computing resources limits. When a function or program 
# finishes its execution, the python interpreter empties the resources taken up 
# by the bits of that function or program and does that using the "garbage
# colector" feature. So variable scope is a feature that makes it simplier for
# the interpreter to do that.
