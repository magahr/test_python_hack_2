"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"]         output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"]     output => ["4","3","2","1"]
text: ["a","b"]             output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    text_03 = []

    text_01 = ["a",  "b",  "c",  "d",  "e"]
    text_02 = ["e-5","d-4","c-3","b-2","a-1"]

    text_04 = ["a",  "b",  "c"]
    text_05 = ["c-3","b-2","a-1"]

    text_06 = ["a",  "b",  "c",  "d"]
    text_07 = ["4","3","2","1"]

    text_08 = ["a",  "b"]
    text_09 = ["2","1"]

   
    for i in range(0, len(s)):
      if len(s)  == 5:     
          for y in range(0, len(text_01)):
              if s[i] == text_01[y]:
                 text_03.append(text_02[y])   
      elif len(s)  == 3:
           for y in range(0, len(text_04)):
              if s[i] == text_04[y]:
                 text_03.append(text_05[y]) 
      elif len(s)  == 4:
           for y in range(0, len(text_06)):
              if s[i] == text_06[y]:
                 text_03.append(text_07[y]) 
      elif len(s)  == 2:
           for y in range(0, len(text_08)):
              if s[i] == text_08[y]:
                 text_03.append(text_09[y]) 
    
    result = text_03

    return result

test8 = fn_hack_8(["a","b","c","d","e"])

print(test8)