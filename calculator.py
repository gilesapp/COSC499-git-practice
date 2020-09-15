print ('This is a test calculator for git practice')

var1 = input('Enter the first number')
var2 = input('Enter the second number')

def addition(v1,v2):
    v1 = var1
    v2 = var2
    v1 += v2
    print('Addition:%d' % v1)


#---------------------------------------
import unittest

unittest.assertEqual(addition(1,2), 3)

if __name__ == '__main__':
    unittest.main()