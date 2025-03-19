

# anive approach
def searchMat(mtx, x):
    for i in range(0, len(mtx)):
        for j in range(0,len(mtx[i])):
            if mtx[i][j]==x:
                return True
            
    return False

matrix1 = [[3,30,38],[20,52,54],[35,60,69]]
print(searchMat(matrix1,33))

# o(n+m) approach

def searchMatrix(mtx, x):
    
    i = 0
    j = len(mtx[0])-1
    
    while j>=0 and i < len(mtx):

        if x > mtx[i][j]:
            i += 1
        
        elif x < mtx[i][j]:
            j -= 1
        
        else:
            return True

    return False


mat = [
    [3, 30, 38],
    [20, 52, 54],
    [35, 60, 69]
]
x = 35
if searchMatrix(mat, x):
    print("true")
else:
    print("false")