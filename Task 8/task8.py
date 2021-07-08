#! /usr/bin/python3

print("content-type: text/html")
print()

import cgi

fs = cgi.FieldStorage()
p_no = fs.getvalue("commands")


if p_no=="SV16 FOX":
   print('''<pre>Name : Rocky
    License No :80819091
    Vehicle Type :MCWG
    Engine No : bhjik2314
    Insurance validity : 7/07/2028</pre>''')

elif p_no=="MH 20EE 7598":
    print('''<pre>Name : Ajay
    License No :20897213
    Vehicle Type :LMV
    Engine No : khgt5677
    Insurance validity : 2/12/2030</pre>''')

else:
    print("No records available")
