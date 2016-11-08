from library import library
list = [
'http://www.allkeyshop.com/blog/buy-battlefield-1-cd-key-compare-prices/',
'http://www.allkeyshop.com/blog/buy-star-wars-battlefront-season-pass-cd-key-compare-prices/',
'http://www.allkeyshop.com/blog/buy-civilization-6-cd-key-compare-prices/',
'http://www.allkeyshop.com/blog/buy-titanfall-2-cd-key-compare-prices/',
'http://www.allkeyshop.com/blog/buy-gta-5-cd-key-compare-prices/'
]
for x, val in enumerate(library):
    val['url-average'] = list[x]
with open('library.txt', 'w') as f:
    f.write('library = ' + str(library))
