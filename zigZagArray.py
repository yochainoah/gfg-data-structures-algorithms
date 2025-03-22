
## naive approach o(nlogn) time complexity and o(1) space complexity
def convertToZigZag(arr):
    ## sort the array and keep it in a new varible
    sorted_arr = sorted(arr)
    ## traverse through the uneven indexes in the array and replace between element i and  i+1
    n = len(sorted_arr)
    for i in range(1, n-2, 2):
        temp = sorted_arr[i]
        sorted_arr[i] = sorted_arr[i+1]
        sorted_arr[i+1] = temp

    return sorted_arr

print(convertToZigZag([1, 4, 5, 3, 2, 6]))

## o(n) approach o(1) space

def zigZagConvert(arr):
    ## define a flag for when to use '<' and when to use '>' in comparison
    flag = False
    n = len(arr)
    ## traverse through the array maintain the order '< > < > < > < ....'
    for i in range(0, n-1):
        ## if flag is False check if arr[i] < arr[i+1]
        if flag == False:
            if arr[i] < arr[i+1]:
                ## change flag to True inorder to check if arr[i] > arr[i+1] next index
                flag = True
            else:
                ## substitute between the two
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                ## and change flag
                flag = True
        else:
            if arr[i] > arr[i+1]:
                ## change flag to False inorder to check if arr[i] < arr[i+1] next index
                flag = False
            else:
                ## substitute between the two
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                ## and change flag
                flag = False
    
    return arr


arr = [4, 3, 7, 8, 6, 2, 1]

print(zigZagConvert(arr))


