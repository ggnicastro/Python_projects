__author__ = 'kaihami'

import os
 new enrollments. All courses already in progress will continue, and each student with a current Enrollment Agreement
Dir = "/home/kaihami/Desktop/RR_files/MAFFT_1_lista/"
Dir_lst = []
for File in os.listdir(Dir):
    if File.endswith(".txt"):
        Dir_lst.append(File)
dup = []
dup2 = []
for path in Dir_lst:
    Open = open(Dir+path, "r").read().split("\n")
    Total = []
    for line in Open:
        lsplit = line.split(",")
        if ("Taxon" not in lsplit and
            (len(lsplit) > 2)):
                Total.append(lsplit)
    for ele in Total:
        locus = ele[6]
        file = ele[-1]
        if locus in dup:
            dup2.append([locus, file])
        if locus not in dup:
            dup.append(locus)
            print locus

for ele in dup2:
    with open("/home/kaihami/Desktop/RR_files/dup.txt", "a") as f:
        f.write(ele[0])
        f.write("\n")

#
"""
Open2 = open("/home/kaihami/Desktop/RR_files/MAFFT_1_lista/Typical_MAFFT_1.txt", "r").read().split("\n")

ALR = []

for line in Open2:
    lsplit = line.split(",")
    if len(lsplit) >2:
        ALR.append(lsplit)
save_path = "/home/kaihami/Desktop/RR_files/Typical_MAFFT_1_sem_dup.txt"
alr_dup = []
alr_dup2 = []
for ele in ALR:
    locus = ele[6]
    if locus in alr_dup:
        alr_dup2.append(locus)
    if locus not in alr_dup:
        alr_dup.append(locus)
        with open(save_path, "a") as f:
            tmp = ele
            for x in xrange(0, len(tmp)):
                if x != (len(tmp)-1):
                    f.write(tmp[x])
                    f.write(",")
                else:
                    f.write(tmp[x])
            f.write("\n")

Check = "/home/kaihami/Desktop/RR_files/Typical_MAFFT_1_sem_dup.txt"
Open_check = open(Check, "r").read().split("\n")

All = []
x = 0
for line in Open_check:
    lsplit = line.split(",")
    if len(lsplit) >2 :
        x += 1
print x
"""