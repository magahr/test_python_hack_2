"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""
def fn_hack_10(text):
    output = []
    count = 1
    for item in text:
        formatted_item = {}
        formatted_item[str(count)] = str(count + 1)
        count += 2
        output.append(formatted_item)
       
    return output

test10 = fn_hack_10([{"a":"b"},{"c","d"},{"e":"f"}])
print(test10)
