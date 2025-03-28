


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


## basically the idea is to find the common letters in both
## so it makes sense to start with the smaller string

## space comlexity o(1) time comlexity o(m+n)

def minCharsToAnagrams(str1, str2):

    ## define a variable to count caracters removed
    min_chars = 0

    ## deifne a variable to store common characters in both strings

    common_chars = 0

    ## traverse through the smallest char

    if len(str1) <= len(str2):

        ## find the common letters
        for i in str1:

            if i in str2:
                common_chars +=1

        min_chars = (len(str2) - common_chars) + (len(str1) - common_chars) 


    else:
        for j in str2:
            if j in str1:
                common_chars += 1
    
        min_chars = (len(str1) - common_chars) + (len(str2) - common_chars) 

    return min_chars





print(minCharsToAnagrams('bcadeh','hea'))
print(minCharsToAnagrams('cddgk','gcda'))
print(minCharsToAnagrams('bca','acb'))