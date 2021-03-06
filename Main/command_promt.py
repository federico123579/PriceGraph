import os
with open("data.txt") as f:
    line = f.readlines()
    price = float(line[-1][11:-1])
    previous_price = float(line[-2][11:-1])
    content = 0
    value = 0
    values = 0
    for x in line:
        try:
            value = float(x.strip('\n')[11:])
        except ValueError:
            pass
        if value != 0:
            values += 1
        else:
            pass
        content = content + value
average = content / values
# Writing
os.system("clear")
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
