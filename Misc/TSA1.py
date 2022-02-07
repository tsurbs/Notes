def flipForBalance(s):
    numFlips = 0
    #approach the list from the left and right sides at once, meeting in the middle at len(s)/2
    for i in range(int(len(s)/2)):        
        if s[i] == "(":
            #in the case of a () match, do nothing to get ()

            #in the case of a (( match, flip one to get ()
            if(s[len(s)-i-1] != ")"):
                numFlips += 1
        else:
            #in the case of a )), flip one to get ()
            if(s[len(s)-i-1] != "("):
                numFlips += 2
            #in the case of a )(, flip both to get ()
            else: numFlips+=1


    return (numFlips)
print(flipForBalance(""))