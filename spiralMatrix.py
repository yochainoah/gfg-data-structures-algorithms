# naive approach o(n*m) time and space complexity

def spiralTraverse(mtx):
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    result = []

    n = len(mtx)
    m = len(mtx[0])

    left = 0
    top = 0
    bottom = n-1
    right = m-1

    index = 0

    r = 0
    c = 0

    visited = [[False] * m for i in range(n)]

    for i in range(n*m):
        result.append(mtx[r][c])
        visited[r][c] = True

        newR = r + dr[index]
        newC= c + dc[index]

        if 0 <= newR <= right and  0 <= newC <= bottom and not visited[newR][newC]:
            r, c = newR, newC

        else:
            index = (index + 1)%4

            r = r + dr[index]
            c = c + dc[index]


    return result


mat = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

result1 = spiralTraverse(mat)
print(result1)

# boundry approach

def boundryTraversal(mtx):
    res = []
    top = 0
    bottom = len(mtx)-1
    left = 0
    right = len(mtx[0])-1

    while left <= right and top <= bottom:
        for i in range(left,right+1):
            res.append(mtx[top][i])
        top+=1
        for i in range(top,bottom+1):
            res.append(mtx[i][right])
        right-=1
        for i in range(right, left-1,-1):
            res.append(mtx[bottom][i])
        bottom-=1
        for i in range(bottom, top-1,-1):
            res.append(mtx[i][left])
        left+=1

    return res

result2 = boundryTraversal(mat)

print(result2)