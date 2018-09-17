x = raw_input ("What is your name: ")
print ("Welcome, " + x)

z = float(input('Enter the length of side "a": '))
y = float(input('Enter the length of side "b": '))

c_squared = z**2 + y**2
c = c_squared**(0.5)

print ('The length of the hypotenuse "c" is: {0}'.format(c))