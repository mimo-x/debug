#coding=utf-8

#原始数据获取
#数据解析
#字符串匹配
#保存到文件
import time
import urllib.request
from bs4 import BeautifulSoup
import re
import xlwt
findlink=re.compile(r'<a href="(.*?)">')   #选择标准
findimage=re.compile(r'<img.*src="(.*?)"',re.S)
findtitle=re.compile(r'<span class="title">(.*)</span>')
findjudge=re.compile(r'<span>(\d)人评价</span>')




def askurl(url):  #访问网址
    head = {
        "User-Agent": " Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }   #head浏览器标识  防止反爬虫
    get=urllib.request.Request(url=url,headers=head)   #传参 就收服务器返回数据
    date=urllib.request.urlopen(get)  #打开页面
    # print(date.read().decode("utf-8"))
    return date
def getdata(url2):
    datalist=[]
    for i in range(0,10):
        start=str(i*25)
        url=url2+start
        html=askurl(url)
        jiexi=BeautifulSoup(html,"html.parser")

        for item in jiexi.find_all('div',class_="item"):
            data=[]
            item=str(item)

            title=re.findall(findtitle,item)[0]
            Link=re.findall(findlink,item)[0]  #寻找符合标准的字符串【0】
            image=re.findall(findimage,item)[0]

            data.append(title)
            data.append(image)
            data.append(Link)
            datalist.append(data)

            print(data)
    print(datalist)
    return datalist

def savedate(datalist):
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet('sheet')
    worksheet.write(0,0,"电影名称")
    worksheet.write(0,1,"电影图片")
    worksheet.write(0,2,"电影链接")
    for x in range(250):
        for y in range(3):
            worksheet.write(x+1,y,datalist[x][y])
        y=0
    workbook.save("douban.xls")

datalist=getdata(r"https://movie.douban.com/top250?start=")
#
savedate(datalist)
