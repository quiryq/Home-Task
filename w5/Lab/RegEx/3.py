import re

txt = input()

def s_search(txt):
    return re.findall("[a-z]+_+[a-z]+", txt)

print(s_search(txt))