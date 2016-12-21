__author__ = 'kaihami'
file_path = open("/home/kaihami/Desktop/Python/Web_scrap2.csv", "r").read().split("\n")

new_lst = []

for line in file_path:
    a = line.split(",")
    new_lst.append(a)

for line in new_lst:
    if len(line) > 7:
        gene = line[0]
        protein = line[7]
        appendFile = open('/home/kaihami/Desktop/RNA-Seq/EDGE-R/26570/26570(2,6)_pJN105(5,6)/fasta_file.txt', 'a')
        before_write = str(gene).replace("'",'').replace("[", "").replace("]", "").replace(" ","")
        before_write2 = str(protein).replace("'",'').replace("[", "").replace("]", "").replace(" ","")
        appendFile.write(">")
        appendFile.write(str(before_write))
        appendFile.write("\n")
        appendFile.write(str(before_write2))
        appendFile.write("\n")
