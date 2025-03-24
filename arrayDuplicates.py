
def findDuplicates(arr):
    ## define a dictionary to store numbers and their instances in array
    hashmap = {}
    n = len(arr)
    ## traverse through array
    for i in range(0, n):
        ## check if element of array exists in hashmap
        if hashmap.get(arr[i]) is not None:
            ## if its value is 1 print element to screen
            if hashmap[arr[i]] == 1:
                print(arr[i])
            ## else add one to ots value in dictionary
            else:
                hashmap[arr[i]] += 1
        ## else initaite the variable with value 1 in dictionary
        else:
            hashmap[arr[i]] = 1

findDuplicates([1, 2, 3, 6, 3, 6, 1])
findDuplicates([1, 2, 3, 4, 3])

## GeeksForGeeks solution same concept
def findDuplicatesGfg(arr):
  
    # Step 1: Create an empty dictionary
    # to store element frequencies
    freqMap = {}
    result = []

    # Step 2: Iterate through the array and
    # count element frequencies
    for num in arr:
        freqMap[num] = freqMap.get(num, 0) + 1

    # Step 3: Iterate through the dictionary to
    # find duplicates
    for key, value in freqMap.items():
        if value > 1:
            result.append(key)

    # Step 4: If no duplicates found, add -1 to the result
    if not result:
        result.append(-1)

    # Step 6: Return the result list containing
    # duplicate elements or -1
    return result