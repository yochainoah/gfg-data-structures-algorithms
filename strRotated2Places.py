## o(n) time complexity  and o(n) space omplexity
def anti_clockwise(str):
    rotated_str = str
    for i in range(2):
        rotated_str = rotated_str[1:] + rotated_str[0]
    return rotated_str

def clockwise(str):
    n = len(str)-1
    rotated_str = str
    for j in range(2):
        rotated_str = rotated_str[n] + rotated_str[:-1]
    
    return rotated_str
def ifRotated(str1, str2):

    # Check if the lengths of the two strings are 
    # not equal, return False if they are not.
    if len(str1) != len(str2):
        return False

    if len(str1) <= 2 or len(str2) <= 2:
        return str1 == str2

    return anti_clockwise(str1) == str2 or clockwise(str1) == str2

print(ifRotated("amazon", "onamaz"))

## o(n) time complexity and o(1) space complexity
def isRotated(str1, str2):
    ## define to flags for checking if str1 rotation of str2
    clockwise = True
    anti_clockwise = True

    if len(str1) != len(str2):
        return False
    ## define var to store string length
    N = len(str1)
    ## loop for clockwise
    for i in range(len(str1)):
        if str1[i] != str2[(i + 2)%N]:
            clockwise = False
            break
    ## loop for anti clockwise
    for i in range(len(str1)):
        if str2[i] !=  str1[(i + 2)%N]:
            anti_clockwise = False
            break

    return anti_clockwise or clockwise