import enchant
d = enchant.Dict("en_US")

def most_common_letter(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

w = ""
let = "qwyuoadfghjzxvbmpn"
for i in range(len(let)):
    for j in range(len(let)):
        for k in range(len(let)):
            for l in range(5):
                for m in range(5):
                    
                    if l != 0 and m != 3:
                        str = let[i]+let[j]+let[k]
                        str = str[:l]+"p"+str[l:]
                        str = str[:m]+"n"+str[m:]
                        # print(str)
                        if d.check(str):
                            w+=(str)
                            print(str)

mcl = most_common_letter(w)
print(mcl)

for i in range(len(mcl)):
    a = max(mcl, key=mcl.get)
    print(mcl.pop(a))

# let = "psfjbia"
# for i in range(len(let)):
#     for j in range(len(let)):
#         for k in range(len(let)):
#             for l in range(len(let)):
#                 for m in range(len(let)):
#                     str = let[i]+let[j]+let[k]+let[l]+let[m]
#                     if d.check(str):
#                         print(str)