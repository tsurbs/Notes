def flipForBalance(s):
    right = 0
    left = 0
    numFlips = 0
    for i in range(int(len(s)/2)):
        print(s[i]+s[len(s)-i-1])
        if s[i] == "(":
            if(s[len(s)-i-1] != ")"):
                numFlips += 1
        else:
            if(s[len(s)-i-1] != "("):
                numFlips += 2
            else: numFlips+=1


    return (numFlips)
print(flipForBalance("(()())"))