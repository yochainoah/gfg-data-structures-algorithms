


# naive approach o(n^2)
def maxSumSubArray(arr):
    max_sum = arr[0]
    max_arr = []
    for i in range(0,len(arr)):
        currSum = arr[i]
        for j in range(i+1,len(arr)):
            currSum = currSum + arr[j]

            max_sum = max(max_sum, currSum)

    return max_sum

print(maxSumSubArray([2,3,-8,7,-1,2,3]))

# kaidens algorithem o(n)

def maxSumSubArrayKaidens(arr):
    maxEnding = arr[0]
    res = arr[0]
    for i in range(1,len(arr)):
        maxEnding = max(maxEnding + arr[i], arr[i])

        res = max(res, maxEnding)
    return res

print(maxSumSubArrayKaidens([2,3,-8,7,-1,2,3]))