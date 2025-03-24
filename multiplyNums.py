## we accept the parameters as strings
def multiply(num1, num2):
    ## define an array to store all the digits of the result
    ## the arrays size will be at most 
    result = [0]*(len(num1) + len(num2))
    num1, num2 = num1[::-1],num2[::-1]

    if num1 == '0' or num2 == '0':
        return 0
    
    ## define a loop to traverse the first number
    for i in range(len(num1)):
        for j in range(len(num2)):
            ## convert both digits to int and store the multiplication in a variable
            digit = int(num1[i]) * int(num2[j])
            ## add the result of the multiplication to result even if its double digits like 12 etc..
            result[i+j] += digit
            ## add the second digit of index i+j in the array to i+j+1
            result[i+j+1] += (result[i+j] // 10)
            ## return index i+j to single digit
            result[i+j] = result[i+j]%10

            print(result)
    result, beg = result[::-1], 0
    while beg < len(result) and result[beg] == 0:
        beg += 1
    
    result = map(str, result[beg:])
    return "".join(result)

   

print(multiply("123", "456"))