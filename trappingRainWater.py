

## naive approach הגעתי לבד
def trappingRainWater(arr):
    ## define a variable to sum all rainwater
    sum = 0
    n = len(arr)
    ## traverse through every element in the array
    for i in range(0,n-1):
    ## find max to the right
        left_max = max(arr[:i+1])
    ## find max to the left
        right_max = max(arr[i:n])
    ## take the minimum of the two 
        min_max = min(right_max, left_max)
        sum += (min_max-arr[i])
        print(sum)

    return sum

print(trappingRainWater([1,2,3,4]))

## two pointer method space complexity o(1) because we have a constant amount of variables
## space complexity o(n) because we are visiting each element once

def maxWater(arr):
    res = 0

    left = 1
    right = len(arr) -2

    maxR = right+1
    maxL = left-1

    while left <= right:

        if maxL <= maxR:
            res += max(0, maxL-arr[left])
            maxL= max(maxL, arr[left])
            left+=1
        else:
            res += max(0, maxR-arr[right])
            maxR = max(maxR, arr[right])
            right-=1
        
        return res