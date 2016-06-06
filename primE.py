'''
Script to find the first prime 
number after dot in exponent.

Created by RinSer

e value taken from wikipedia
'''


import math


# Exponent value from wiki
e = '2,7182818284 5904523536 0287471352 6624977572 4709369995 9574966967 6277240766 3035354759 4571382178 5251664274 2746639193 2003059921 8174135966 2904357290 0334295260 5956307381 3232862794 3490763233 8298807531 9525101901 1573834187 9307021540 8914993488 4167509244 7614606680 8226480016 8477411853 7423454424 3710753907 7744992069 5517027618 3860626133 1384583000 7520449338 2656029760 6737113200 7093287091 2744374704 7230696977 2093101416 9283681902 5515108657 4637721112'

def prime_search(number, length):
    '''
    Function to test n-digit
    numbers for primality in
    string consisting of integers.
    
    Receives a string of digits 
    and tested numbers length int.
    
    Returns the first found prime.
    '''
    assert(length > 0)
    for i in range(len(number)):
        num = ''
        for j in range(length):
            if (i+j)<len(number):
                num += number[i+j]
        # Convert string to int
        num = int(num)
        ceil = int(math.ceil(math.sqrt(num)))
        # Primality test
        for c in range(2, ceil+1):
            if num%c==0:
                break
            else:
                if c==ceil:
                    # assert(num == 7427466391)
                    return num
    # Prime has not been found
    return 'Not found'
                    
                    
# Omit all non-digits in e
exp = ''
for i in range(len(e)):
    if e[i]!=',' and e[i]!=' ':
        exp += e[i]

# Execute search and return result
print prime_search(exp, 10)