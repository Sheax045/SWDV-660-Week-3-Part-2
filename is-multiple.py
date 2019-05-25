##code determines if the number n is a multiple of the number m.

n = int(input('Give me a number: '))
m = int(input('Give me a second number: '))

def is_multiple(n, m):
    
    if n % m == 0:
        print( 'True,', n, 'is a multiple of', m)
    
    else:
        print('False,', n, 'is not a multiple', m)
    
is_multiple(n, m)
