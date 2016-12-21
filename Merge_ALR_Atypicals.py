__author__ = 'kaihami'

import os

Dir = "/home/kaihami/Desktop/RR_files/MAFFT_1_lista/"

dir_lst = []

for File in os.listdir(Dir):
    if File.endswith(".txt"):
        dir_lst.append(File)
for path in dir_lst:
    Open = open(Dir+path, "r").read().split("\n")
    All_prot = []
    for line in Open:
        lsplit = line.split(",")
        if len(lsplit) > 2:
            All_prot.append(line)
            if "Taxon" not in lsplit:
                with open("/home/kaihami/Desktop/RR_files/Total_Proteins_MAFFT_1.txt", "a") as f:
                    f.write(line)
                    f.write("\n")

Check = open("/home/kaihami/Desktop/RR_files/Total_Proteins_MAFFT_1.txt", "r").read().split("\n")
All = []
x = 0
for line in Check:
    lsplit = line.split(",")
    if len(lsplit) > 2:
        All.append(lsplit)

All_dct = {}
dup = []
dup2 = []

for line in All:
    locus = line[6]
    if locus in dup:
        dup2.append(locus)
        print locus
    if locus not in dup:
        dup.append(locus)
        print locus

