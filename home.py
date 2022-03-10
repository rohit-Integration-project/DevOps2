#!/usr/bin/python3

import cgi
import subprocess as sp

print("content-type:  text/html")
print()

#print("hello World !!")
form= cgi.FieldStorage()
cmd=form.getvalue("y")

out = sp.getoutput(cmd)

print(out)
