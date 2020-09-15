print ('This is a test calculator for git practice')

var1 = float(input('Enter the first number:'))
var2 = float(input('Enter the second number:'))

def addition(v1,v2):
    v1 += v2
    return v1
    
print('Addition: %s' % addition(var1,var2))


#-------------------unittest-----------------------------
#----Addition----
#assert addition(1,2) == 3
#assert addition(1,4) == 4




