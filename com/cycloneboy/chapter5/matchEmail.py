import  re

patter = "\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*" # 匹配电子邮件的正则表达式
string = "<a href='http://www.baidu.com'>百度首页</a/><br><a href='mailto:c-e+o@iqi-anyue.com.cn'>电子邮件</a>"
result = re.search(patter,string)
print(result)