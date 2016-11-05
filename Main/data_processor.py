import  datetime, schedule, sys, time
#import schedule
sys.path.insert(0, 'Modules')
import priceExtractor as pe
import library as lib
# Collect Data
def collect_data():
    now = datetime.datetime.now()
    with open("data.txt") as f:
        lines = f.readlines()
        # If Yes
        if int(lines[-1][8:10]) == int(now.day):
            pass
        # If No
        else:
            for x in range(len(lib.library)):
                if x == 0:
                    price = pe.import_price(lib.library[x]['url'])
                else:
                    price = str(price) + ',' + str(pe.import_price(lib.library[x]['url']))

            # Write Data
            with open("data.txt", "a") as f:
                f.write('%02d' % now.year + '-' + '%02d' % now.month + '-' + '%02d' % now.day + ',' + price + "\n")

if __name__ == '__main__':
    #schedule.every().day.at("10:30").do(job)
    collect_data()
