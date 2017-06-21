import urllib.request

url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
# 模拟浏览器的 User-Agent
headers =("User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
           "(KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36")

# opener = urllib.request.build_opener()
# opener.addheaders = [headers]
#
# # 出错
# data = opener.open(url).read()

# 添加报头
req = urllib.request.Request(url)
req.add_header('User-Agent',"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
           "(KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36")
data = urllib.request.urlopen(req).read()

# 保存网页到D盘
fhandle = open("D:/python/download/myweb/part4/3.html","wb")
fhandle.write(data)
fhandle.close()


#file = urllib.request.urlopen(url)
