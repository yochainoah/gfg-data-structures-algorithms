
## naive approach finding all subarrays of size k and then finding the minimum average of them
## o(n*k) time complexity and o(1) space compexity
def minSubArr(arr,k):
    ## defining a variable to store sub array
    
    ## define a variable to hold min average
    min_avg = max(arr)
    print(min_avg)
    min_arr = []
    ## traverse through the indexes 0 until (len(arr)-k)
    for i in range(0,len(arr)-k+1):
        sub_arr = []
        sum = 0
        ## traverse through every sub array that starts from i until i+k
        for j in range(i,i+k):
            sum += arr[j]
            sub_arr.append(arr[j])
        ## calculate average if average is smaller then previous average then replace it 
        average = sum//k
        if average < min_avg:
            min_arr = sub_arr
            min_avg = average
    
    print(min_avg)
    return min_arr

print(minSubArr([3, 7, 90, 20, 10, 50, 40],3))


## optimal solution o(n) time complexity and o(1) space complexity
def slidingWindowAlgo(arr, k):
    ## define a variable to store the sub array we currently at
    curr_arr = arr[:k]
    ## define a variable 
    min_arr = curr_arr
    ## define a variable to store the length of the array
    n = len(arr)
    first_index = 0
    last_index = k-1
    while last_index < n:
        if sum(curr_arr) < sum(min_arr):
            min_arr = curr_arr
        
        first_index+=1
        last_index+=1
        curr_arr = arr[first_index:last_index+1]

    return min_arr

print(slidingWindowAlgo([1, 12, -5, -6, 50, 3, 0, -45, 23], 4))
