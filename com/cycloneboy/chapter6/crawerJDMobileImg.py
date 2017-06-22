import  re
import  urllib.request
import  urllib.error

def craw(url,page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div id="plist".+? <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    pat2 = '<img width="220" height="220" data-img="1" src="//(.+?\.jpg)">'
    imageList = re.compile(pat2).findall(result1)
    x = 1
    for imageUrl in imageList:
        imageName = "D:/python/download/myweb/part6/imgJDMobile/" + str(page) +"_"+ str(x)+".jpg"
        imageUrl = "http://" + imageUrl
        try:
            urllib.request.urlretrieve(imageUrl,filename=imageName)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1

for i in range(1,10):
    url = "http://list.jd.com/list.html?cat=9987,653,655&page=" + str(i)
    craw(url,i)