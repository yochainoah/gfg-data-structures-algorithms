## well basically the algorithm is to replace each character with all of the characters in the string
## and then storing every permutation in an array
## o(n^2) time complexity and o(n!) space comlexity
def permutations(str):
    ## define an array to store all permutations 
    perms = []

    ## define a copy of the string
    str_copy = str
    ## traverse every char in array
    print(len(str))
    for i in range(0, len(str)):
        ## strings are unmuttable!!
        for j in range(0, len(str)):
            ## convert the string into an array inorder to 
            ## be able to swap between the characters
            str_array = list(str)
            print(len(str_array), str_array)
            ## the first assignment doesent override str_array[i] because of a concept in python called tuple unpacking
            str_array[i], str_array[j] = str_array[j], str_array[i]
            perms.append(''.join(str_array))

    
    return perms


print(permutations('ABC'))

## o(n*n!) time complexity 
## if I want to keep an array that stores results through recursion I gotta keep it as a parameter
# Python Program to generate all unique
# permutations of a string

# Recursive function to generate 
# all permutations of string s
def recurPermute(index, s, ans):

    # Base Case
    if index == len(s):
        ans.append("".join(s))
        return

    # Swap the current index with all
    # possible indices and recur
    for i in range(index, len(s)):
        s[index], s[i] = s[i], s[index]
        recurPermute(index + 1, s, ans)
        s[index], s[i] = s[i], s[index]

# Function to find all unique permutations
def findPermutation(s):

    # Stores the final answer
    ans = []

    recurPermute(0, list(s), ans)

    # sort the resultant list
    ans.sort()

    return ans

if __name__ == "__main__":
    s = "ABC"
    res = findPermutation(s)
    for x in res:
        print(x, end=" ")