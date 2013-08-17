# -*- coding: UTF-8 –*-
import urllib2
import re

enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://proxy.tencent.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

html = urllib2.urlopen("http://www.baidu.com").read()
html=html.replace('\n', '')
html+="<A HREF='hello'>xxx</a>"
aList=re.findall(r'(<(a|A).*?(href|HREF)=.*?>.*?</(a|A)>)',html)
for a in aList:
    print a[0]


