import re

txt = input()

def s_search(txt):
    return re.findall("a.*b", txt)

print(s_search(txt))