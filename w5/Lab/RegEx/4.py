import re

txt = input()

def foo(txt):
    return re.findall("[A-Z]{1}[a-z]+", txt)

print(foo(txt))