import urllib, json, os, sys,datetime
sys.path.insert(0, 'Modules')
import priceExtractor as pe
# Collect Data
now = datetime.datetime.now()
with open("data.txt") as f:
    lines = f.readlines()
    # If Yes
    if int(lines[-1][8:10]) == int(now.day):
        price = float(lines[-1][11:-1])
        previous_price = float(lines[-2][11:-1])
    # If No
    else:
        price = pe.import_price()
        previous_price = float(lines[-1][11:-1])
        # Write Data
        with open("data.txt", "a") as f:
            f.write('%02d' % now.year + '-' + '%02d' % now.month + '-' + '%02d' % now.day + ';' + str(price) + "\n")
with open("data.txt") as f:
    line = f.readlines()
    content = [float(x.strip('\n')[11:]) for x in line]
    average = sum(content) / len(content)
# Writing
os.system("cls")
dic = {
'\\' : b'\xe2\x95\x9a',
'-'  : b'\xe2\x95\x90',
'/'  : b'\xe2\x95\x9d',
'|'  : b'\xe2\x95\x91',
'+'  : b'\xe2\x95\x94',
'%'  : b'\xe2\x95\x97',
}

percentage_diff = round((price - previous_price) / previous_price * 100, 2)
percentage_average_diff = round((price - average) / average * 100, 2)
#discount =

def decode(x):
    return (''.join(dic.get(i, i.encode('utf-8')).decode('utf-8') for i in x))
print(decode('+------------------------------------%'))
print(decode('|           Battlefield 1            |') + "\tinstant-gaming: %.2f" % price)
print(decode('|               ') + "%.2f" % price + decode('                |') + "\tPrevious: %.2f" % previous_price)
print(decode('\\------------------------------------/') + "\tDifference: %.2f" % (percentage_diff) + '%')
print(decode('+------------------------------------%'))
print(decode('|        Average of Prices           |') + "\tinstant-gaming: " + "%.2f" % round(average, 2))
print(decode('|               ') + "%.2f" % round(average, 2) + decode('                |') + "\tDifference: %.2f" % (percentage_average_diff) + '%')
print(decode('\\------------------------------------/'))
