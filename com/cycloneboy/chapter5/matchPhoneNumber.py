import  re

pattern = "\d{4}-\d{7}|\d{3}-\d{8}" # 匹配电话号码的正则表达式
string = "021-672826647474744477472001048520"
result = re.search(pattern,string)
print(result)