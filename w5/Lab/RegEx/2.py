import re

txt = input()

def s_search(txt):
    return re.search(".*abbb?.*", txt)

print("YES" if s_search(txt) else "NO")