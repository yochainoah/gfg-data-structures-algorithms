
## define a function that accepts two parameters
def lcs(str1, str2, n, m):
    ## base case:
    ## if any of the strings reaches length 0
    if n == 0 or m == 0:
        return 0
    
    ## if the last characters of the string are equal we will return 1 and call
    ## the function without the last character in both
    if str1[n-1] == str2[m-1]:
        return 1 + lcs(str1, str2, n, m)
    
    ## else return the max between lcs(str1, str2, n-1, m) and lcs(str1, str2, n, m-1)
    else:
        # If the last characters do not match
        # Recur for two cases:
        # 1. Exclude the last character of S1 
        # 2. Exclude the last character of S2 
        # Take the maximum of these two recursive calls
        return max(lcs(str1, str2, n-1, m), lcs(str1, str2, m-1))
    

## Dynamic programming approach

def longestCommonSubstr(str1, str2):
    dp = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]

    for i in range(len(str1) - 1, -1, -1):
        for j in range(len(str2) -1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])

    
    return dp[0][0]