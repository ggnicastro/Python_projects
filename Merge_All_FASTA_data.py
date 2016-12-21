__author__ = 'kaihami'

"""
Merge all Fasta file
"""

import os

Dir = "/home/kaihami/Desktop/RR_files/Final_REC/"

Dir_lst = []
with open("/home/kaihami/Desktop/RR_files/Total_REC.txt", "a") as f:
    f.write("Taxon,Bacteria,Bacteria2,Phylym,Genome_ID,CDS,RR_class,Locus_tag,UID,Fasta,Hit,Start,End,E_val,Short,REC_sequence")
    f.write("\n")
for File in os.listdir(Dir):
    if File.endswith(".txt"):
        Dir_lst.append(File)
for ele in Dir_lst:
    Open = open(Dir + ele, "r").read().split("\n")
    total = []
    for line in Open:
        lsplit = line.split(",")
        if lsplit > 4 and lsplit[0] != "Taxon":
            total.append(lsplit)

    with open("/home/kaihami/Desktop/RR_files/Total_REC.txt", "a") as f:
        for ele in total:
            for x in xrange(0, len(ele)):
                if x != (len(ele)-1):
                    f.write(ele[x])
                    f.write(",")
                else:
                    f.write(ele[x])
            f.write("\n")

#Check

Check = open("/home/kaihami/Desktop/RR_files/Total_REC.txt", "r").read().split("\n")
Check_ls = []
for line in Check:
    lsplit = line.split(",")
    if len (lsplit) > 3:
        Check_ls.append(lsplit)
        with open("/home/kaihami/Desktop/RR_files/Total_REC2.txt", "a") as f:
            f.write(line)
            f.write("\n")

Check2 = open("/home/kaihami/Desktop/RR_files/Total_REC2.txt", "r").read().split("\n")