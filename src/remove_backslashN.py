import sys

def remove(file_name_in, file_name_out):
    f_in = open(file_name_in, 'r')
    f_out = open(file_name_out, 'w')

    lines_in = f_in.read().splitlines()
    for line_in in lines_in:
        elements = line_in.split()
        if(len(elements) != 0):
            f_out.write(elements[0] + '\t' + elements[1] + '\n')
        #print(line_in.split())
    
    f_in.close()
    f_out.close()


if __name__ == '__main__':
    remove(sys.argv[1], sys.argv[2])
    print("file written in " + sys.argv[2])