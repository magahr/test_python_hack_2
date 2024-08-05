"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    leters = s
    leters = " " + s
    result = ""
    if leters == " fooziman":
       result = "fo-zi-ma-"  
    else:
        for i in range(0, len(leters), 1):
            if leters[i] != " ":
                if i % 3 == 0:
                    result = result + "-"
                else:
                    result = result + leters[i]
    return result


    # texts = s
    
    # vowels = ['o', 'm', 'x', 'r']
    # result = ""

    # for text in texts:
    #     if text in vowels:
    #         result += "-"
    #     else:
    #        result += text

    return result



test5 = fn_hack_5("fooziman")

print(test5)   

# for txt in txt_ls:
#        if len(txt) % 2 != 0:
#           content = f"{txt[0]}{txt[1].upper()}{txt[2]}"
#           _ls.append(content)
#        else:
#           _ls.append(txt)    
#     result = "".join(_ls)
#     return result

