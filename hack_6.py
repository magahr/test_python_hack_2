"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    text_03 = []
    text_01 = ["a","b","c","d","e"]
    text_02 = ["1","-","3","-","5"]
    for i in range(0, len(s)):
        for y in range(0, len(text_01)):
            if s[i] == text_01[y]:
               text_03.append(text_02[y])   
    
    if text_03 == []:
       text_03.append("0")  
    result = text_03
    return result

test6 = fn_hack_6("")

print(test6)
