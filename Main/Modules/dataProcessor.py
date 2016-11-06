import  datetime, schedule, sys, time
#import schedule
import priceExtractor as pe
import library as lib
import converter
# Collect Data
def collect_data(link_to_file):
    now = datetime.datetime.now()
    with open(link_to_file) as f:
        lines = f.readlines()
        # If Yes
        if int(lines[-1][8:10]) == int(now.day):
            converter.delete_last_line('data.txt')
        # If No
        else:
            pass
        for x in range(len(lib.library)):
            if x == 0:
                price = pe.import_price(lib.library[x]['url'])
            else:
                price = str(price) + ',' + str(pe.import_price(lib.library[x]['url']))

        # Write Data
        with open(link_to_file, "a") as f:
            f.write('%02d' % now.year + '-' + '%02d' % now.month + '-' + '%02d' % now.day + ',' + price + "\n")

if __name__ == '__main__':
    #schedule.every().day.at("10:30").do(job)
    collect_data('../data.txt')
