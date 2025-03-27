from functools import reduce

## my idea: find the repeating string and check if the string is the multiplication of that
## in addition if the length of the string is a prime number theres no chance its a substring repetition
## so maybe we can find all of the strings divisors and check if each substring to see if the string is a multiplication of that 



## function to find all factors of a number
def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
print(factors(7))

## define a function 
def substringRep(str):

    ## define a var n to store string length
    n = len(str)

    factor_list = list(factors(n))
    print("factorlist:", factor_list)
    ## now if foctors(n) is equal only to 1 and n then n is a prime
    ## and we can return false
    if len(factor_list) == 2 and factor_list[0] == 1 and factor_list[1] == n:
        return False
    
    ## if not we will have to traverse through all of the factors except for 1 and n and see
    ## if str is a multipication of a substring with the length of that substring
    ## which means that if we multiply the substring with its matching factor it will give us the str
    else:
        for i in factor_list:
            print("substr",str[:i], "n//i:", (n//i))
            if i == 1 or i == n:
                continue
            if str[:i] * (n//i) == str:
                return True

    return False

print(substringRep('aabaabaabaabaab'))

    

