#This is the official webpage from python https://www.python.org/
#Python don't support multi-line comments but ignore strings without a variable assigned
"""
    Like this, Python ignore
"""
import constantes

a = "Hello world"

print(a + " " + str(constantes.PINUMBER))

#Constant variable puts in another file named modules and write in uppercase.
#Import .py file with name of the file and when you put one variable or function write first filename.variable

a = 12 #integer
b = True #boolean
c = 12.23 #float
d = [2,3,4] #list
e = "Python"
print(type(a))

print(f"Hello, {e}")
print("Hola familia")