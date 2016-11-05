import fileinput, library
def convert():
    file_data = fileinput.input("../data.txt", inplace=True)
    new_line = 'Date'
    for x in range(len(library.library)):
        new_line = new_line + ',' + library.library[x]['name']
    with open('../data.txt') as f:
        line_test = f.readline()
        print line_test
    for line in file_data:
        if line_test == line:
            print new_line
        else:
            print line.strip('\n')
if __name__ == '__main__':
    convert()
