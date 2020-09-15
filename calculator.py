print ('This is a test calculator for git practice')

op = float(input('Select the operation you would like to perform:\nAddition: 1   Subtraction: 2\n'))
var1 = float(input('Enter the first number:'))
var2 = float(input('Enter the second number:'))


def addition(v1,v2):
    v1 += v2
    return v1

def subtraction(v1,v2):
    v1 -= v2
    return v1
    
if op == 1:
    print('Addition: %s' % addition(var1,var2))
elif op == 2:
    print('Subtraction: %s' % subtraction(var1,var2))
else:
    print('invalid operaion selection')


#-------------------unittest-----------------------------
#----Valid assertion----
#assert addition(var1,var2) == var1 + var2
#assert subtraction(var1,var2) == var1 - var2

#----Error assertion----
#assert addition(1,2) == -1
#assert subtraction(1,4) == -2




