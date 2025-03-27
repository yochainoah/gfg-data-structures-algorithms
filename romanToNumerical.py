

## define a function to return the value representing each symbol
def value(s):
    if s == 'I':
        return 1
    
    if s == 'V':
        return 5
    
    if s == 'X':
        return 10
    
    if s == 'L':
        return 50
    
    if s == 'C':
        return 100
    
    if s == 'D':
        return 500
    
    if s == 'M':
        return 1000
    
    return -1


def convertToNumerical(roman):
    if len(roman) <= 1:
        return value(roman)
    
    if len(roman) == 2:
        if value(roman[0]) < value(roman[1]):
            return value(roman[1]) - value(roman[0])
        
        if value(roman[0]) >= value(roman[1]):
            return value(roman[1]) + value(roman[0])
    numeric_value = 0
    i = 0
    while i < len(roman):
        s1 = roman[i]

        if i < len(roman) - 1:
            s2 = roman[i + 1]
            if value(s1) < value(s2):
                numeric_value += value(s2) - value(s1)
                i += 1
            else:
                numeric_value += value(s1)
            
        else:
            numeric_value += value(s1)
        i+=1

    return numeric_value

print(convertToNumerical('MCMIV'))
            

