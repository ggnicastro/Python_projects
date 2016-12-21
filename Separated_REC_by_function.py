__author__ = 'kaihami'
import os
dir = "/home/kaihami/Desktop/RR_files/Final_REC/"
REC_file_lst = []

for File in os.listdir(dir):
    if File.endswith(".txt"):
        REC_file_lst.append(File)

for path in REC_file_lst:
    Open_File = open(dir+path, "r").read().split("\n")
    Total = []
    print dir+path
    for ele in Open_File:
        lsplit = ele.split(",")
        if len(lsplit) > 2:
            Total.append(lsplit)
    for line in Total:
        tmp = []
        Tax = line[0]
        Bac = line[1]
        Bac2 = line[2]
        Phy = line[3]
        Genome_ID = line[4]
        CDS = line[5]
        RR_fun = line[6].replace("/", "-").replace("\\", "-")
        locus = line[7]
        Uid = line[8]
        Fasta = line[9]
        Hit = line[10]
        St = line[11]
        End = line[12]
        E_val = line[13]
        Short = line[14]
        REC_seq = line[15]
        tmp.extend((Tax, Bac, Bac2, Phy, Genome_ID, CDS, RR_fun, locus, Uid, Fasta, Hit, St, End, E_val, Short, REC_seq))
        save_path = "/home/kaihami/Desktop/RR_files/REC_Final_By_domain/"
        with open(save_path+RR_fun+".txt", "a") as f:
            for pos in xrange(0, len(tmp)):
                if pos != (len(tmp)-1):
                    f.write(tmp[pos])
                    f.write(",")
                else:
                    f.write(tmp[pos])
            f.write("\n")
