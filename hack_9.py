"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    text = s
    output = {}
    for key, value in text.items():
        if key.lower() == "foo":
            output["Foo"] = value.capitalize()[0:3] + value[4:9]
    return output


test9 = fn_hack_9({"foo": "fookziman", "bar": "barziman"})

print(test9)