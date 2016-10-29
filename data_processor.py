import urllib, json, os, sys
from pprint import pprint
import datetime
# Collect Data
url = "https://extraction.import.io/query/extractor/d00472f3-457e-4b37-b710-4002797e3087?_apikey=ab96cf38f5fe40e69b3ae0a59c9a2711840b0bee59bd951f25b9a2ee4e2c9d05e7e5e29ae414029bf21cbc3f161452143630d8125cf5572ebcb9b321ffd4ac087ef33b9bcf6ad7330418ebdb43e2243e&url=https%3A%2F%2Fwww.instant-gaming.com%2Fit%2F1421-comprare-key-origin-battlefield-1%2F"
new_number_choice = raw_input("Do you want to record a new value?(y/n)\n")
# If Yes
if new_number_choice == "y":
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    price_str = json.dumps(data["extractorData"]["data"][0]["group"][0]["Price"][0]["text"])
    price = float(price_str[1:-7])
    with open("data.txt") as f:
        lines=f.readlines()
        print lines[-1][11:-1]
# Write Data
    now = datetime.datetime.now()
    with open("data.txt", "a") as myfile:
            myfile.write(str(now.year) + '-' + str(now.month) + '-' + str(now.day) + ';' + str(price) + "\n")
# If No
elif new_number_choice == "n":
    with open("data.txt") as f:
        lines=f.readlines()
        price = float(lines[-1][11:-1])
        previous_price = float(lines[-2][11:-1])
with open("data.txt") as f:
    content = [float(x.strip('\n')[11:]) for x in f.readlines()]
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
percentage_diff = round((previous_price - price) / previous_price * 100, 2)
percentage_average_diff = round((average - price) / average * 100, 2)
def decode(x):
    return (''.join(dic.get(i, i.encode('utf-8')).decode('utf-8') for i in x))

print(decode('+------------------------------------%'))
print(decode('|       Best Price of the Day        |') + "\tinstant-gaming: " + str(price))
print(decode('|               ' + str(price) + '                |') + "\tPrevious: " + str(previous_price))
print(decode('\\------------------------------------/') + "\tDifference: %.2f" % (percentage_diff) + '%')
print(decode('+------------------------------------%'))
print(decode('|        Average of Prices           |') + "\tinstant-gaming: " + str(round(average, 2)))
print(decode('|               ' + str(round(average, 2)) + '                |') + "\tDifference: %.2f" % (percentage_average_diff) + '%')
print(decode('\\------------------------------------/'))
