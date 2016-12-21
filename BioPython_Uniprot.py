__author__ = 'kaihami'
from urllib2 import urlopen
import time
"""
    From the ALR file (plos Pathogen) find each ALR gene in UniProt database,
    Return:
    use: "http://www.uniprot.org/uniprot/C5P6L0.tab"
    Entry	Entry_name	Status	Protein_names	Gene_names	Organism	Length
    pick: 0(nome), 2(status), 3(protein),  5(organism) => se deletado 3 = Deleted
    use: "http://www.uniprot.org/uniprot/C5P6L0.fasta"
    Fasta Head  Fasta Seq
"""

write_file = "/home/kaihami/Desktop/ALR/ALR_Genes_format.txt"


first_line = "Entry,Status,Organism,FASTA"
with open(write_file, 'a') as f:
    f.write(first_line)
    f.write("\n")


gene_file_path = "/home/kaihami/Desktop/ALR/ALR_Genes.txt"
gene_file = open(gene_file_path, 'r').read().split('\n')
x = 0
for gene in gene_file:
    time.sleep(1)
    x+=1
    gene_name = gene.split("_")
    try:
        url_tab = urlopen("http://www.uniprot.org/uniprot/" +gene_name[0] +".tab")


        page_tab = url_tab.read()
        page_tab2 = page_tab.split("\n") #0: head 1: info
        page_tab_info = page_tab2[1].split("\t") #split info

        Entry, Status, Status2, Organism = page_tab_info[0], page_tab_info[2], page_tab_info[3], page_tab_info[5]

        if "Deleted." in Status2:
            status_final = "Deleted"
        else:
            status_final = Status

        url_fasta = urlopen("http://www.uniprot.org/uniprot/" +gene_name[0] +".fasta")
        page_fasta = url_fasta.read()
        page_fasta2 = page_fasta.split("\n")
        page_fasta_format = page_fasta2[1:-1]
        fasta = "".join(page_fasta_format)
        #write down
        a = ",". join([Entry, status_final, Organism,fasta])
        with open(write_file, "a") as f:
            f.write(a)
            f.write("\n")
        print a
    except:
        with open(write_file, "a") as f:
            f.write(gene_name[0])
            f.write(",ERROR")
            f.write("\n")
    print "LEFT:", (str(len(gene_file)-x))
    print "_"*40