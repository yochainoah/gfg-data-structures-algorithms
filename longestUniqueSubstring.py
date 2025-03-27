
## o(26*n) time complexity because the inner loop will run at most 26 times
## o(26) space complexity 
## because they are 26 unique chrarcters in the alphabet
def longestUniqueSubstr(str):
    ## define a variable to store maxSubstring
    maxSubstrLength = 0
    # maxSubstr = ''

    ## traverse the whole string to define where we start the sub string
    for i in range(len(str)):
        ## define a string to store the current substring
        substr = '' 
        ## define a hashmap to store the counts fo each character
        hashmap = {}
        for j in range(i, len(str)):
            hashmap[str[j]] = 1 + hashmap.get(str[j], 0)
            if hashmap[str[j]] > 1:
                break
            else:
                substr += str[j]
        
        ## check if current substring is bigger the max substring
        if len(substr) >= maxSubstrLength:
            maxSubstr = substr
            maxSubstrLength = len(substr)
 
    return maxSubstrLength, maxSubstr
    

    
print(longestUniqueSubstr('geeksforgeeks'))
print(longestUniqueSubstr('abcdefabcbb'))

## sliding window approach o(n) time complexity
def longestSubstr(str):
    ## define an in to keep result
    res = 0
    ## converting string to array of chars
    str_array = list(str)
    ## defining starting index of sliding window 
    l = 0
    ## defining ending index of sliding window
    r = 0
    ## defining an array to keep track of visited letters
    vis = [False]*26
    
    while r < len(str_array):

        while vis[ord(str_array[r]) - ord('a')] == True:
            vis[ord(str_array[l]) - ord('a')] = False
            l += 1

        vis[ord(str_array[r]) - ord('a')] = True

        res = max(res, r - l + 1)

        r+=1

        

    return res


print(longestSubstr('geeksforgeeks'))