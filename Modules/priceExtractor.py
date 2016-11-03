'''import urllib2
import xml.etree.ElementTree as ET
# Not Module
url = "https://www.instant-gaming.com/it/1421-comprare-key-origin-battlefield-1/"
req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
html = urllib2.urlopen(req).read()
with open("response.html", "w") as f:
    f.write(html)
root = ET.parse('response.html')
root.findall('//*[@id="ig-product-main-panel-boxprice-contentright-price]')'''
from xml import html
import requests
