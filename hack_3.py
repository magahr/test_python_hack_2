"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    leters1 = ["a","e","i","o","u","q","x","n","f","b"]
    leters2 = ["@","3","¡","0","v","Q","X","N","F","B"]
    
    for leter0 in result:
        for i in range(len(leters1)):
            if leter0 == leters1[i]:
               result  = result.replace(leters1[i],leters2[i]) 
    return result


# result = "fooziman"
#     result_ultimo = result[7:8]
#     result =  result[0:7] + result_ultimo.upper()
#     return result
# result = result.upper()

test3 = fn_hack_3("qux")

print(test3)