


## my approach: checking if both strings have the same length
## then I can sort the strings and if they are the same then they are anagrams

def anagrams(str1, str2):
    
    ## if the strings dont have the same length I can
    ## return false

    if len(str1) != len(str2):
        return False
    
    ## sort both strings
    sorted_str1 = ''.join(sorted(str1))
    sorted_str2 = ''.join(sorted(str2))

    ## check if both strings are equal
    if sorted_str1 == sorted_str2:
        return True
    
    return False

print(anagrams('geeks', 'ksreg'))

