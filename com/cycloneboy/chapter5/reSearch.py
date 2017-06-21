import  re
string = "hellomypythonispythonnourpythonend"
pattern = ".python."
result = re.match(pattern,string)
result2 = re.search(pattern,string)

print(result)
print(result2)