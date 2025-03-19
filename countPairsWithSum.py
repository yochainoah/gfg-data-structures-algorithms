
## naive approach o(n^2) time complexity

def findPairs(arr, target):
    # intialize counter to count pairs with sum
    count = 0
    n = len(arr)
    ## iterate through the array for the first number in pair
    for i in range(n):
        ## iterate through the array for the second number in pair
        for j in range(i+1,n):
            ## sum the two numbers
            ## check if numbers equal target and add to count if they do
            if arr[i]+arr[j] == target:
                count+=1


    ## return count
    return count


print(findPairs([1, 5, 7, -1, 5],6))


## two pointer approach
## o(nlogn) + o(n) time complexity
## o(1) space complexity because we are not using any extra data structures and are varaiables are a constant number
## o(nlogn) because sorted has a time complexity of o(nlogn)
## and two pointer has a time complexity of o(n) because we pass through every element in the array at most once
def maxPairs(arr, target):
    ## initialize counter 
    count = 0
    ## sort the array 
    sorted_array = sorted(arr)
    # print(sorted_array)
    ## initialize L and R
    left = 0
    right = len(arr)-1
    n=len(arr)
    ## traverse through the array as long as left <= right
    while left < right:
        if sorted_array[left]+sorted_array[right] < target:
            left+=1
        elif sorted_array[left]+sorted_array[right] > target:
            right-=1
        else:
            ## count all instances of that pair in array
            element1 = sorted_array[left]
            element2 =  sorted_array[right]
            cnt1 = 0
            cnt2 = 0

            ## search for all instances of first element in pair
            while left <= right and sorted_array[left] == element1:
                left+=1
                cnt1+=1

            ## search for all instances of second element in pair
            while left <= right and sorted_array[right] == element2:
                right -= 1
                cnt2 += 1
            ## if element1 equal to element to add sum of n
            # natural numbers of cnt1 to count (we are only counting cnt1
            # because if elements are equal only left will traverse through the array)
            if element1 == element2:
                count += cnt1*(cnt1-1) // 2
            # if the elements in the pair are not equal add product of cnt1 and cnt2 to count
            else:
                count += (cnt1*cnt2)


                
    return count
    

print(maxPairs([1, 5, 7, -1, 5],6))

def maxPairsMap(arr, target):
    ## define a map for the occurence of each number in the array
    hashMap = {}
    ## define count for the pairs
    count = 0
    ## traverse every element in the  array
    for i in range(len(arr)):
        ## find compliment element to current element
        other = target-arr[i]
        ## check if compliment element exists in hashmap
        ## if it does update count with number of ocurrences of compliment element in the array
        ## and update number of ocurrences of element by 1
        if hashMap[other]:
            count += map[other]
        ##instantiate arr[i] in hashmap to 1 or add 1 if arr[i] exists in map
        ## .get(key, default_value) returns the value associated with key if exists and 0 if not
        hashMap[arr[i]] = hashMap.get(arr[i],0)+1

    return count