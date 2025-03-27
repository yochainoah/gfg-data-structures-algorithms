



def lookAndSay(n):

    ## initialize 2nd term
    s = '11'


    for i in range(3 ,n + 1):


        ## initialize count for count instances of each digit
        cnt = 1

        ## initialize variable to store the previous term
        temp = ''
        ## add '$' so the loop runs one extra time
        s += '$'
        ## traverse the current term will be dependent on traversing the previous term
        m = len(s)
        for j in range(1, m):

            if s[j] != s[j - 1]:
                temp += str(cnt)
                temp += s[j - 1]

                cnt = 1
            else:
                cnt += 1

        s = temp 
    return s

print(lookAndSay(5))