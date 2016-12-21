__author__ = 'kaihami'
"""
Ok!
"""
import os

save_path = "/home/kaihami/Desktop/RR_files/ALR_MAFFT_1.txt"

with open(save_path, "a") as f:
    f.write("Taxon,Bacteria,Phylum,Genome_ID,CDS,RR_Class,Locus_tag,UID,Fasta,REC_seq,D_1,D_2,D_3,B4, B5,All,Type")
    f.write("\n")

Open_RR = open("/home/kaihami/Desktop/RR_files/Final_REC/Total_REC.txt", "r").read().split("\n")

Total_RR = []

for line in Open_RR:
    lsplit = line.split(",")
    if len(lsplit) >2:
        Total_RR.append(lsplit)

Dir_ALR = "/home/kaihami/Desktop/RR_files/MAFFT_1_lista/Separated_by_conservation/ALR/"

ALR_lst = []

for File in os.listdir(Dir_ALR):
    if File.endswith(".txt"):
        ALR_lst.append(File)
x = 0
for path in ALR_lst:
    Open = open(Dir_ALR+path, "r").read().split("\n")
    Alr = []
    for line in Open:
        lsplit = line.split(",")
        if len(lsplit) > 2:
            Alr.append(lsplit)

    for ele in Alr:
        locus = ele[0]
        D_1 = ele[7]
        D_2 = ele[8]
        D_3 = ele[9]
        B4 = ele[10]
        B5 = ele[11]
        All = ele[12]

#Open file:

        for line in Total_RR:
            Taxon = line[0]
            Bacteria = line[1]
            Phylum = line[3]
            Genome_ID = line[4]
            CDS = line[5]
            RR_Class = line[6]
            Locus_tag = line[7]
            UID = line[8]
            Fasta = line[9]
            REC_seq = line[-1]
            Atypical = "ALR"
            if locus == Locus_tag:
                #print line
                print locus, "=", Locus_tag
                tmp = []
                tmp.extend((Taxon, Bacteria, Phylum, Genome_ID, CDS, RR_Class, Locus_tag, UID, Fasta, REC_seq, D_1, D_2, D_3, B4, B5, All, Atypical))
                with open(save_path, "a") as f:
                    for x in xrange(0, len(tmp)):
                        if x != (len(tmp)-1):
                            f.write(tmp[x])
                            f.write(",")
                        else:
                            f.write(tmp[x])
                    f.write("\n")

A = open("/home/kaihami/Desktop/RR_files/ALR_MAFFT_1.txt", "r").read().split("\n")
x = 0
for line in A:
    lsplit = line.split(",")
    if len(lsplit) > 2:
        x+=1
        print x

print "Total =", x