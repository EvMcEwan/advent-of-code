"""
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""

d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
x = 0
y = 0

x += 123
y += 456
d += x & y
e += x | y
f += x << 2
g += y >> 2
h += -x
if h < 0:
    h += 65535
i += -y
if i < 0:
    i += 65535


print("d", d)
print("e", e)
print("f", f)
print("g", g)
print("h", h)
print("i", i)
print("x", x)
print("y", y)
