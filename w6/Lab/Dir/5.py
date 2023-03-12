import os
color = ["colum", "word", "number"]
with open('s.txt', "w") as fr:
        for i in color:
                fr.write("%s\n" % i)
content = open('s.txt')
print(content.read())