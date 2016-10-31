import urllib, json, os, sys
sys.path.insert(0, 'Modules')
import librarian
import datetime
# Collect Data
url = "https://extraction.import.io/query/extractor/518ceba2-e6e0-46d5-b607-170fb36c5108?_apikey=ab96cf38f5fe40e69b3ae0a59c9a2711840b0bee59bd951f25b9a2ee4e2c9d05e7e5e29ae414029bf21cbc3f161452143630d8125cf5572ebcb9b321ffd4ac087ef33b9bcf6ad7330418ebdb43e2243e&url=https%3A%2F%2Fwww.instant-gaming.com%2Fit%2F1421-comprare-key-origin-battlefield-1%2F%3Fcurrency%3DEUR"
now = datetime.datetime.now()
with open("data.txt") as f:
    lines = f.readlines()
    # If Yes
    if int(lines[-1][8:10]) == int(now.day):
        price = float(lines[-1][11:-1])
        previous_price = float(lines[-2][11:-1])
    # If No
    else:
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        price_str = json.dumps(data["extractorData"]["data"][0]["group"][0]["Price"][0]["text"])
        #discount = float(json.dumps(data["extractorData"]["data"][0]["group"][0]["Dicount"][0]["text"])[1:])
        price = float(price_str[1:-7])
        previous_price = float(lines[-1][11:-1])
        # Write Data
        with open("data.txt", "a") as f:
            f.write(str(now.year) + '-' + str(now.month) + '-' + str(now.day) + ';' + str(price) + "\n")
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
