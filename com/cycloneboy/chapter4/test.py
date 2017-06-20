import urllib.request

file = urllib.request.urlopen("http://www.baidu.com")

data = file.read()
dataline = file.readline()
print(dataline)

print(data)

#保存网页到D盘
fhandle =open("D:/python/download/myweb/part4/1.html","wb")
fhandle.write(data)
fhandle.close()

#直接爬取网页到D盘
filename = urllib.request.urlretrieve("http://edu.51cto.com",
                                      filename="D:/python/download/myweb/part4/2.html"
                                      )

#清除URLretrieve执行所造成的缓存
urllib.request.urlcleanup()
