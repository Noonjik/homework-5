#string power
def string_power(string, power):
    if power>0:
        result = power*string
    elif power == 0:
        result = ' '
    else:
        root = ''
        for i in range(0, len(string)//-(power)):
            root += string[i]
        if root*(-power) == string:
            result = root
        else:
            result = 'Not defined'
    return result

if __name__ == '__main__':
    test1 = 'ab'
    pow1 = 1
    print (string_power(test1, pow1))
    test2 = 'abc'
    pow2 = 0
    print (string_power(test2, pow2))
    test3 = 'xyzxyz' 
    pow3 = -2
    print (string_power(test3, pow3))
    test4 = 'xyzxyz' 
    pow4 = -3
    print (string_power(test4, pow4))
    test5 = 'xyzxyz' 
    pow5 = -1
    print (string_power(test5, pow5))
