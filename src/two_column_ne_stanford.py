import sys
# Tsha 
def two_columns_without_underscore(file_name, file_name_out):
    """
    before
    Mary/PERSON Barra/PERSON appointed/O as/O General/ORGANIZATION Motors/ORGANIZATION chief/O December/O 10/O ,/O 2013/O The/O United/LOCATION States/LOCATION 's/O largest/O car/O manufacturer/O General/ORGANIZATION Motors/ORGANIZATION today/O named/O Mary/PERSON Barra/PERSON as/O its/O new/O chief/O executive/O ./O  
    """
    f = open(file_name, 'r')
    lines = f.read().splitlines()
    f.close()
    out = open(file_name_out, 'w')

    for line in lines:
        for word_chunk in line.split():
                out.write(word_chunk.replace('/', '\t') + '\n')
        out.write('\n')

    out.close()

if __name__ == '__main__':
    #sys.argv[1] # le fichier stanford a convertir pour qu'il y ait :
    # mot\tcategorie
    file_name_out = sys.argv[1][:-2]
    print(file_name_out)
    lines = two_columns_without_underscore(sys.argv[1], file_name_out)