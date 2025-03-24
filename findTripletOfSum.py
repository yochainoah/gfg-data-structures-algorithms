
## naive approach o(n^3) time complexity and o(1) space complexity
def findTripletOfSum(arr, target):
    ## define a variable to store the sum of 3 elements in array
    sum_of_three = 0
    n = len(arr)
    ## define an array to store triplet
    result = []
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                result = [arr[i], arr[j], arr[k]]
                sum_of_three = arr[i] + arr[j] + arr[k]
                if sum_of_three == target:
                    return result
    
    result = [-1]
    return result

print(findTripletOfSum([1, 4, 45, 6, 10, 8], 13))
print(findTripletOfSum([1, 2, 4, 3, 6, 7], 10))


## o(n^2) time complexity approach  
def tripletSum(arr, target):
    ## define L and R for two pointer approach
    l = 0
    r = len(arr)
    ## define a flag to check if target was found
    found = False
    ## sort the array
    arr.sort()
    ## define a variable to store sum
    curr_sum = 0
    ## traverse the array using the two pointer approach
    while l < r-2:
        curr_sum = arr[l] + arr[r-1]
        ## if left plus right and minimum element between them is greater then target move left one step forward
        # print(arr[l+1:r])
        if curr_sum + min(arr[l+1:r]) > target:
            r -= 1
        ## if left plus right and maximum element between them is smaller then target move right one step backwards
        elif curr_sum + max(arr[l+1:r]) < target:
            l += 1
        ## else the third element must be some where in between!!
        else:
            for i in range(l+1, r):
                if curr_sum + arr[i] == target:
                    return True

    return False
                
print(tripletSum([1, 4, 45, 6, 10, 8], 13))
print(tripletSum([1, 2, 4, 3, 6, 7], 10))
print(tripletSum([1, 2, 4, 3, 6, 7], 25))


