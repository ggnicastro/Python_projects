__author__ = 'kaihami'
"""
Format MAFFT output in Locus, alignment
"""

import os
dir = "/home/kaihami/Desktop/RR_files/REC_Final_By_domain/REC_FASTA_2/MAFFT_out/Done/"
dir_out = "/home/kaihami/Desktop/RR_files/REC_Final_By_domain/REC_FASTA_2/MAFFT_out/MAFFT_Reformated/"
MAFFT_file_lst = []
for File in os.listdir(dir):
    MAFFT_file_lst.append(File)


for path in MAFFT_file_lst:

    fi1 = open(dir+path, "r").read().split("\n")
    for x in xrange(0, len(fi1)):
        a = []
        line = fi1[x]
        if line.startswith(">"):
            tmp = []
            print line
            for y in xrange(x+1, len(fi1)):
                line2 = fi1[y]
                if ">" not in line2:
                    tmp.append(line2)
                if ">" in line2:
                    break
            final = "".join(tmp)
            a.extend((line.replace(">",""), final, path))
        with open(dir_out + path + "_reformat.txt", "a") as f:
            for pos in xrange(0, len(a)):
                if pos != (len(a)-1):
                    f.write(a[pos])
                    f.write(",")
                else:
                    f.write(a[pos])
            f.write("\n")
