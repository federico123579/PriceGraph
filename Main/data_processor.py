import  datetime, schedule, sys, time, schedule
sys.path.insert(0, 'Modules')
import priceExtractor as pe
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
            price = pe.import_price()
            previous_price = float(lines[-1][11:-1])
    # Write Data
    with open("data.txt", "a") as f:
        f.write('%02d' % now.year + '-' + '%02d' % now.month + '-' + '%02d' % now.day + ',' + str(price) + "\n")

if __name__ == '__main__'
schedule.every().day.at("10:30").do(job)
