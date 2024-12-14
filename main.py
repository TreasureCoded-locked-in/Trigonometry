from inspect import Parameter


math.function_name(Parameter)

# or import the math module

import math
import math

print(math.degrees((math.pi/2)))
print(math.radians(60))

import math

print(math.sin(math.pi/3)) #pi/3 radians is converted to 60 degrees
print(math.tan(math.pi/3))
print(math.cos(math.pi/6))

import math

print(math.asin(1))
print(math.acos(0))
print(math.atan(1))

import cmath

x = 1.0
y = 1.0
z = complex(x,y)

print ("The arc sine is: ",cmath.asin(z))
print ("The arc cosine is: ",cmath.acos(z))  
print ("The arc tangent is: ",cmath.atan(z))

import cmath

x = 1.0
y = 1.0
z = complex(x,y)
print ("The hyperbolic sine is : ",cmath.sinh(z))
print ("The hyperbolic cosine is : ",cmath.cosh(z))  
print ("The hyperbolic tangent is : ",cmath.tanh(z))

import cmath

x = 1.0
y = 1.0
z = complex(x,y)

print ("The inverse hyperbolic sine is : ",cmath.asinh(z))
print ("The inverse hyperbolic cosine is : ",cmath.acosh(z))  
print ("The inverse hyperbolic tangent is : ",cmath.atanh(z))