import codecs
#import pandas as pd
import csv

def read_path(extension):
    file_path = input(f"Caminho do arquivo {extension}: ")

    if file_path[-3:] != extension:
        print(f"O arquivo precisa ser do tipo {extension}")
        exit()

    return file_path

def read_file():
    file_path = read_path("txt")

    try:
        file = codecs.open(file_path, "r", "utf-8")
        lines = file.readlines()
    except:
        print("Não foi possível ler o arquivos.")
        return

    for index, line in enumerate(lines):
        #removendo a quebra de linha
        lines[index] = line.replace("\n", "")
        print(f"{index + 1} - {lines[index]}")

    file.close()

def wirte_file():
    file_path = read_path("txt")
    
    str_list = []
    str_list.append(input("Dado 1: "))
    qtdItens = 0
    
    while str_list[-1] != "EOF":
        qtdItens += 1
        str_list.append( input(f"Dado {qtdItens+1}: ") )
    
    str_list.pop()

    file = codecs.open(file_path, "w", "utf-8")
    for item in str_list:
        file.write(f"{item}\n")

    file.close()

def read_csv():
    # df = pd.read_csv('teste.csv', header = None)
    # rows = df.values
    # for index, row in enumerate(rows):
    #     row[-1] = row[-1].replace("\n", "")
    # print(rows)

    file_path = read_path("csv")
    file = codecs.open(file_path, "r", "utf-8")
    lines = list(csv.reader(file))
    print(lines)

def write_csv():
    file_path = read_path("csv")

    itens = []
    numRows = int(input("Digite a quantidade de linhas: "))

    for i in range(0, numRows):
        name = input("Digite o nome: ")
        age = input("Digite a idade: ")
        city = input("Digite a cidade: ")
        data_to_insert = [name, age, city]
        itens.append(data_to_insert)

    file = codecs.open(file_path, "w", "utf-8")
    writer = csv.writer(file)
    
    for row in itens:
        writer.writerow(row)
    
    file.close()

def list_file_names():
    from os import walk
    
    dir_path = input("Digite o caminho da pasta: ") 
    #function walk goes through every subfolder, so it is necessary to iterate in each folder
    for(dir_path, dir_names, files) in walk(dir_path):
        for file in files:
            print(file)


if __name__ == '__main__':
    #read_file()
    #wirte_file()
    #read_csv()
    #write_csv()
    list_file_names()