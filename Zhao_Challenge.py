#The Legs
print("Input lengths of the triangle sides: ")
x = float(input("Side One: "))
y = float(input("Side Two: "))
z = float(input("Side Three: "))

   
xsq = float(x)**2
ysq = float(y)**2   
zsq = float(z)**2

#Adding of the legs
xy = float(xsq) + float (ysq) 

if x + float(y) < float(z):
    print "This isn't a triangle chief, goodbye."
elif xy == float(zsq):
    print "This is a right triangle"
elif xy < float(zsq):
    print "This is an obtuse triangle"
elif xy > float(zsq):
    print "This is an acute triangle"
    
    