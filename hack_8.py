"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"]         output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"]     output => ["4","3","2","1"]
text: ["a","b"]             output => ["2","1"]
"""


def fn_hack_8(s):
   
    text = s
    output = []
    count = len(text)
    for i in range(count, 0, -1):
        # if i == count:
        if count % 2 == 0:
            # output.append(f'{text[i-1]}-{i}')
            output.append(f'{i}')
        else:
            # output.append(f'{text[i-1]}-{i+1}')
            output.append(f'{text[i-1]}-{i}')
    result = output

    return result

test8 = fn_hack_8(["a","b","c","d","e"])

print(test8)