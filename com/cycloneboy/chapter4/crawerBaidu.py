import urllib.request

keywd = "盛磊"
url = "http://www.baidu.com/s?wd="
# 转码
key_code = urllib.request.quote(keywd)
url_all = url + key_code

req = urllib.request.Request(url_all)
data = urllib.request.urlopen(req).read()

# 保存到D盘
fhandle = open("D:/python/download/myweb/part4/4.html","wb")
fhandle.write(data)

fhandle.close()