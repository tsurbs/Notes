import requests as re 
import json
min = 0
max = 0
k = 1000000/2
for i in range(1000000):
    
    r0 = re.get('https://www.quizdb.org/api/tossups/'+str(i)).status_code
    r1 = re.get('https://www.quizdb.org/api/tossups/'+str(i+1)).status_code
    r2 = re.get('https://www.quizdb.org/api/tossups/'+str(i+2)).status_code
    r3 = re.get('https://www.quizdb.org/api/tossups/'+str(i+3)).status_code
    r4 = re.get('https://www.quizdb.org/api/tossups/'+str(i+4)).status_code
    if(i%50 == 0):
        print(i)
    for r in [r0,r1,r2,r3,r4]:
        if r != 404:
            if i>max:
                print("max", i)
                max = i
            if i<min:
                print("min", i)
                min = i
    i+=5
print(min,max)

