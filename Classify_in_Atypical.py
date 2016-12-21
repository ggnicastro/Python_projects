__author__ = 'kaihami'
"""
Ok!
"""
import os

save_path_typical = "/home/kaihami/Desktop/RR_files/Typical_MAFFT_1.txt"
save_path_atypical = "/home/kaihami/Desktop/RR_files/Atypical_MAFFT_1.txt"
save_path_atypical2 = "/home/kaihami/Desktop/RR_files/Atypical(D1)_MAFFT_1.txt"
other = "/home/kaihami/Desktop/RR_files/Other_RR.txt"

with open(save_path_typical, "a") as f:
    f.write("Taxon,Bacteria,Phylum,Genome_ID,CDS,RR_Class,Locus_tag,UID,Fasta,REC_seq,D_1,D_2,D_3,B4, B5,All,Type")
    f.write("\n")

with open(save_path_atypical, "a") as f:
    f.write("Taxon,Bacteria,Phylum,Genome_ID,CDS,RR_Class,Locus_tag,UID,Fasta,REC_seq,D_1,D_2,D_3,B4, B5,All,Type")
    f.write("\n")
with open(save_path_atypical2, "a") as f:
    f.write("Taxon,Bacteria,Phylum,Genome_ID,CDS,RR_Class,Locus_tag,UID,Fasta,REC_seq,D_1,D_2,D_3,B4, B5,All,Type")
    f.write("\n")

Open_RR = open("/home/kaihami/Desktop/RR_files/Final_REC/Total_REC.txt", "r").read().split("\n")

Total_RR = []

for line in Open_RR:
    lsplit = line.split(",")
    if len(lsplit) >2:
        Total_RR.append(lsplit)

Dir_ALR = "/home/kaihami/Desktop/RR_files/MAFFT_1_lista/Separated_by_conservation/Conserverd_D/"

ALR_lst = []
D1_typical = ["D", "E"]
D2_typical = ["D", "E"]
D3_typical = ["D", "E"]
B4_typical = ["S", 'T']
B5_typical = ["K"]
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
        All = D_1 + D_2 + D_3 + B4 + B5

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
                if D_3 not in D3_typical:
                    print locus, "=", Locus_tag, "ALR"
                    print All
                    tmp = []
                    tmp.extend((Taxon, Bacteria, Phylum, Genome_ID, CDS, RR_Class, Locus_tag, UID, Fasta, REC_seq, D_1, D_2, D_3, B4, B5, All, "ALR"))
                    with open(other, "a") as f:
                        for x in xrange(0, len(tmp)):
                            if x != (len(tmp)-1):
                                f.write(tmp[x])
                                f.write(",")
                            else:
                                f.write(tmp[x])
                        f.write("\n")
                if ((D_2 not in D2_typical) or
                    (B4 not in B4_typical) or
                    (B5 not in B5_typical)
                    ):
                        #print line
                        print locus, "=", Locus_tag, "Atypical"
                        print All
                        tmp = []
                        tmp.extend((Taxon, Bacteria, Phylum, Genome_ID, CDS, RR_Class, Locus_tag, UID, Fasta, REC_seq, D_1, D_2, D_3, B4, B5, All, "Atypical"))
                        with open(save_path_atypical, "a") as f:
                            for x in xrange(0, len(tmp)):
                                if x != (len(tmp)-1):
                                    f.write(tmp[x])
                                    f.write(",")
                                else:
                                    f.write(tmp[x])
                            f.write("\n")
                if D_1 not in D1_typical:
                    if D_2 in D2_typical:
                        print locus, "=", Locus_tag, "D1"
                        print All
                        tmp = []
                        tmp.extend((Taxon, Bacteria, Phylum, Genome_ID, CDS, RR_Class, Locus_tag, UID, Fasta, REC_seq, D_1, D_2, D_3, B4, B5, All, "D1_Atypical"))
                        with open(save_path_atypical2, "a") as f:
                            for x in xrange(0, len(tmp)):
                                if x != (len(tmp)-1):
                                    f.write(tmp[x])
                                    f.write(",")
                                else:
                                    f.write(tmp[x])
                            f.write("\n")
                if (D_1 in D1_typical and
                        (D_2 in D2_typical) and
                        (D_3 in D3_typical) and
                        (B4 in B4_typical) and
                        (B5 in B5_typical)):
                            print locus, "=", Locus_tag, "Typical"
                            print All
                            tmp = []
                            tmp.extend((Taxon, Bacteria, Phylum, Genome_ID, CDS, RR_Class, Locus_tag, UID, Fasta, REC_seq, D_1, D_2, D_3, B4, B5, All, "Typical"))
                            with open(save_path_typical, "a") as f:
                                for x in xrange(0, len(tmp)):
                                    if x != (len(tmp)-1):
                                        f.write(tmp[x])
                                        f.write(",")
                                    else:
                                        f.write(tmp[x])
                                f.write("\n")

"""
A = open("/home/kaihami/Desktop/RR_files/Typical_MAFFT_1.txt", "r").read().split("\n")
x = 0
for line in A:
    lsplit = line.split(",")
    if len(lsplit) > 2:
        x+=1
        print x

print "Total =", x
"""
x = 0
for path in ALR_lst:
    Open = open(Dir_ALR+path, "r").read().split("\n")
    Alr = []
    for line in Open:
        lsplit = line.split(",")
        if len(lsplit) > 2:
            x+=1
        print x
print "Total =", x