import  re

pattern = "[a-zA-Z]+://[^\s]*[.com|.cn]" # 匹配网址
string = "<a href='http://www.baidu.com'>百度首页</a>"
result = re.search(pattern,string)
print(result)
