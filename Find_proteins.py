__author__ = 'kaihami'

"""
Find proteins with a determined domain
"""
import os
domain = "NarLfamily(REC-HTH)"
dr = "/home/kaihami/Desktop/RR_files/Fasta/"
dr2 = "/home/kaihami/Desktop/RR_files/Fasta/FASTA_NarL/"
REC_file_lst = []
for File in os.listdir(dr):
    if File != "notes" and File != "FASTA_NarL" and File != "Only_fasta_seq":
        REC_file_lst.append(File)
x = 0
for ele in REC_file_lst:
    path = ele
    print path
    to_open = open(dr+path, "r").read().split("\n")
    total = []
    for line in to_open:
        lsplit = line.split(",")
        if len(lsplit) >2:
            total.append(lsplit)
    for level in total:
        if "Taxonomy" not in level:
            if level[6] == domain:
                x +=1
                print level[6]
                locus = level[7]
                fasta = level[-1]
                print locus, fasta
                save_path = (dr2+"FASTA_All")
                with open(save_path, "a") as f:
                    f.write(">")
                    f.write(str(locus))
                    f.write("\n")
                    f.write(str(fasta))
                    f.write("\n")
                    f.write("\n")
print "finish"
