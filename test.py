'''
https://mail.python.org/archives/list/python-ideas@python.org/message/3IY3NTJRAMSQZYTCVQABTYPM2TGS3UVN/
'''

from itertools import product
import complex_math

pz = 0.0
cs = [complex(*t) for t in product((pz, -pz), repeat=2)]
cs_om = [complex_math.ComplexNumber(complex_math.RECT, *t) for t in product((pz, -pz), repeat=2)]

pads = [15,15,15,20,20]

for (x, y, z), (w, v, u) in zip(product(cs, repeat=3), product(cs_om, repeat=3)):
    t1 = (x*y)*z
    t2 = x*(y*z)
    t3 = (w*v)*u
    t4 = w*(v*u)
    if repr(t1) != repr(t2) or repr(t3) != repr(t4):
        if repr(t1) != repr(t2):
            print("old error")
        if repr(t3) != repr(t4):
            print("new error")

        print("old out default  ", end=' ')
        for a, pad in zip([x,y,z,t1,t2], pads):
            print(str(a).ljust(pad), end='')
        print()

        print("new out default  ", end=' ')
        for a, pad in zip([w,v,u,t3,t4], pads):
            print(str(a).ljust(pad), end='')
        print()

        print("new out to rect  ", end=' ')
        for a, pad in zip([w,v,u,t3,t4], pads):
            print(str(a.as_rect()).ljust(pad), end='')
        print()

        print("new out to polar ", end=' ')
        for a, pad in zip([w,v,u,t3,t4], pads):
            print(str(a.as_polar()).ljust(pad), end='')
        print()

        print()