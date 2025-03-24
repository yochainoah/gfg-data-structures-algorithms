

def atoi(number):
    ## start index to define where to start after the spaces
    index = 0
    ## variable to store sign
    sign = 1
    ## a variable to store the result
    result = ''
    ## loop to find where digits start in string
    while number[index].isspace():
        index+=1

    ## condition to check if first index in digits is + or -
    if number[index] == '-':
        sign = -1
        index+=1
    ## traverse the entire number until a non-digit number is encountered or we each the end of the string 
    while index < len(number) and number[index].isdigit():
        result += number[index]
        index+=1

    result = int(result)*sign
    if result > 2**31 - 1:
        return 2**31 - 1
    if result < -2**31:
        return -2**31
    return result
print(atoi("-333353524531231231jh231311133ahghvvckg"))
