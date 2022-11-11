f = open("level1.txt","r")
t = f.read()
str1 =""
for i in t:
    if i == "+":
        str1 = str1 + "#"
    else:
        str1 = str1 + i
print(str1)