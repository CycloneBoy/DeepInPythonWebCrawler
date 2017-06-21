import  re

# re.match 和 re.searsh 的区别
string = "hellomypythonispythonnourpythonend"
pattern = ".python."
result = re.match(pattern,string)
result2 = re.search(pattern,string)

print(result)
print(result2)

# 全局匹配函数
result3 = re.compile(pattern).findall(string)
print(result3)

# re.sub 匹配替换函数
pattern1 = "python."
result4 = re.sub(pattern1,"php",string) # 默认全部替换
result5 = re.sub(pattern1,"php",string,2) # 最多匹配两次

print(result4)
print(result5)