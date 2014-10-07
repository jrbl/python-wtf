WTF is a Python library that tries to help you understand where things
came from. It's intended for manual tracing of executing programs. Anywhere
one would otherwise be using print statetments, one can instead use wtf
statements.

Simply calling wtf() defaults to printing the name of the current function
and wtf line number and the function names and line numbers of the previous
four stack frames.

You can configure where output gets written to, how many stack frames
to examine, and whether or not to inspect variable declarations as it walks
up the stack.

