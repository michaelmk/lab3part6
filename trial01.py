import math
x=('''
      A
     A A
    A   A
   AAAAAAA
  A       A
 A         A
A           A
''')
txt = x.replace("A","H")
print(txt)
x=('''
H       H
H       H
HHHHHHHHH
H       H
H       H
''')
print(x)
x = 3+4-6/2*3
print(x)
x=12%5
print(x)
y=4
x=y<<2
print(x)
x=3
y=++x+4//x
print(x)
y=7
x=2*y<y
print(x)
x=5
x*=3**x
print(x)
a = float(input("values of a:"))
b = float(input("values of b:"))
c = float(input("values of c:"))
X = (-b + math.sqrt(b*b- 4*a*c)) / (2*a)
Y = (-b - math.sqrt(b*b- 4*a*c)) / (2*a)
print("when a = ","%.2f" % a,", b = ","%.2f" % b,", c = ","%.2f" % c,": X = ","%.2f" % X," or ","%.2f" % Y)
