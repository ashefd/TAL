import sys
import csv

def extract_ne(file_name):
    f = open(file_name, "r")
    words = f.read().split()
    print(words)
    dict_occurences = {}
    dict_ne = {}
    for w in words :
        m = w.split("/")
        key = m[0]
        value = m[1]
        if value != "O" and key in dict_occurences.keys():
                dict_occurences[key] = dict_occurences[key] + 1
        elif value != "O" :
                dict_occurences[key] = 1
                dict_ne[key] = value

    return dict_occurences, dict_ne, len(words)

def create_ne_rows(dict_occurences, dict_ne, size):
    rows = [["Entite nommee",  "Type",  "Nombre d’occurrences", "Proportiondans le texte (%)"]]
    for key in dict_occurences.keys() :
        rows.append([key, dict_ne[key], dict_occurences[key], (dict_occurences[key]/size) * 100 ])
    return rows

def write_rows_in_file(file_name_out, rows):
    with open(file_name_out+".csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


if __name__ == '__main__':
    dict_occurences, dict_ne, size = extract_ne(sys.argv[1])
    rows = create_ne_rows(dict_occurences, dict_ne, size)
    write_rows_in_file(sys.argv[2], rows)