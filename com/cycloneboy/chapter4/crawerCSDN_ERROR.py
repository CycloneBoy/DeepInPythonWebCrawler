import urllib.error

try:
    urllib.request.urlopen("http://blogss.csdn.net")
except urllib.error.HTTPError as e:
    print(e.reason)
except urllib.error.URLError as e:
    print(e.reason)

# URLError 是 HTTPError 的父类
try:
    urllib.request.urlopen("http://blogss.csdn.net")
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reson"):
        print(e.reason)