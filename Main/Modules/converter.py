import fileinput, library
def convert(link_to_file):
    file_data = fileinput.input(link_to_file, inplace=True)
    new_line = 'Date'
    for x in range(len(library.library)):
        new_line = new_line + ',' + library.library[x]['name']
    with open(link_to_file) as f:
        line_test = f.readline()
        print line_test
    for line in file_data:
        if line_test == line:
            print new_line
        else:
            print line.strip('\n')
def delete_last_line(link_to_file):
    with open(link_to_file, 'r') as f:
        lines = f.readlines()
    with open(link_to_file, 'w') as f:
        f.writelines([item for item in lines[:-1]])

if __name__ == '__main__':
    convert("../data.txt")
