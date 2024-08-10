"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    text_03 = []
    text_01 = ["a","b","c","d","e"]
    text_02 = ["1", 2 ,"3", 4 ,"5"]
    for i in range(0, len(s)):
      for y in range(0, len(text_01)):
        if s[i] == text_01[y]:
           text_03.append(text_02[y])   

    if text_03 == []:
       text_03.append(0)       
    result = text_03
    return result

test7 = fn_hack_7("d")

print(test7)
