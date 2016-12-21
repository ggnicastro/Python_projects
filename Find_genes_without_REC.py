__author__ = 'kaihami'

"""
Find Proteins without REC domain
Input:RR_fasta_Alpha_formated2.txt
"""

import os

#Count all proteins

Dir = "/home/kaihami/Desktop/RR_files/Fasta/"
All_REC_files = []

for File in os.listdir(Dir):
    if File.endswith(".txt"):
        All_REC_files.append(File)
Total_Proteins = []
for fi in All_REC_files:
    Open_File = open(Dir+fi, "r").read().split("\n")
    All_elements = []
    for ele in Open_File:
        esplit = ele.split(",")
        if len(esplit) > 2:
            All_elements.append(esplit)
    print fi
    for line in All_elements:
        Bacteria = line[1]
        Locus_tag = line[7]
        if Bacteria == "Bacteria":
            pass
        else:
            Total_Proteins.append(Locus_tag)

#Find proteins with more than one REC domain
#from this Dir /home/kaihami/Desktop/RR_files/Final_REC/dup/old/

Dir_2 = "/home/kaihami/Desktop/RR_files/Final_REC/dup/old/"
Total_REC_dir = []
for File2 in os.listdir(Dir_2):
    if File2.endswith(".txt"):
        Total_REC_dir.append(File2)

Total_REC = []
for ele in Total_REC_dir:
    Open = open(Dir_2 + ele, "r").read().split("\n")
    Parial = []
    for line in Open:
        lsplit = line.split(",")
        if len(lsplit) > 2:
            Parial.append(lsplit)
    for Line in Parial:
        Bac = Line[1]
        Locus_tag_REC = Line[7]
        if Bac == "Bacteria":
            pass
        else:
            Total_REC.append(Locus_tag_REC)
domains in the Final_REC file => this file contains all information + REC domain information
output a file containg the locus_tag
dup = []
dup2 = []

for Ele in Total_REC:
    if Ele in dup:
        dup2.append(Ele)
    if Ele not in dup:
        dup.append(Ele)
    print Ele
print "finish"
len(dup2) + len(dup)
len(dup2)
Save_dup = "/home/kaihami/Desktop/RR_files/Prot_mais_de_um_REC.txt"

with open(Save_dup, "a") as f:
    for line in dup2:
        f.write(line)
        f.write("\n")
Genes_with_no_REC = []
Genes_with_no_REC2 = []

for line in Total_Proteins:
    locus = line
    if locus in dup:
        Genes_with_no_REC.append(locus)
    if locus not in dup:
        Genes_with_no_REC2.append(locus)
    print locus
print "finish"

Save_no = "/home/kaihami/Desktop/RR_files/Prot_sem_REC.txt"

with open(Save_no, "a") as f:
    for line in Genes_with_no_REC2:
        f.write(line)
        f.write("\n")

