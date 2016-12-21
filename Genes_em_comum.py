__author__ = 'kaihami'


lst_1 = open("/home/kaihami/Desktop/RNA-Seq/EDGE-R/21550_sRNA_final/21550_sem_sRNA_up.txt", "r").read().split("\n")
lst_2 = open("/home/kaihami/Desktop/RNA-Seq/EDGE-R/21550_sRNA_final/21550_sRNA_up.txt", "r").read().split("\n")

comum = []
only_1 = []
only_2 = []
for gene in lst_1:
    if gene in lst_2:
        if gene not in comum:
            comum.append(gene)
    else:
        only_1.append(gene)

comum2 = []
for gene in lst_2:
    if gene in lst_1:
        if gene not in comum2:
            comum2.append(gene)
    else:
        only_2.append(gene)

for line in comum:
    load = open("/home/kaihami/Desktop/RNA-Seq/EDGE-R/21550_sRNA_final/comum.txt", "a")
    to_write = str(line).replace("'",'').replace("[", "").replace("]", "").replace(" ","")
    load.write(to_write)
    load.write("\n")
    load.close()

for line in only_1:
    load = open("/home/kaihami/Desktop/RNA-Seq/EDGE-R/21550_sRNA_final/Sem_sRNA.txt", "a")
    to_write = str(line).replace("'",'').replace("[", "").replace("]", "").replace(" ","")
    load.write(to_write)
    load.write("\n")
    load.close()

for line in only_2:
    load = open("/home/kaihami/Desktop/RNA-Seq/EDGE-R/21550_sRNA_final/Com_sRNA.txt", "a")
    to_write = str(line).replace("'",'').replace("[", "").replace("]", "").replace(" ","")
    load.write(to_write)
    load.write("\n")
    load.close()