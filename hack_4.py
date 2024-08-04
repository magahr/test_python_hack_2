"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    for leter0 in result:
        if leter0 == "f" or leter0 == "b" or leter0 == "n":
           result  = result.replace(leter0,"") 
    return result
    

test4 = fn_hack_4("barziman")

print(test4)