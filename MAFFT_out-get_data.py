__author__ = 'kaihami'
"""
Format MAFFT output (without \n), and get conserved residues
"""
import os
def Open_MAFFT(File):
    tmp = []
    for line in File:
        lsplit2 = line.split(",")
        if len(lsplit2) >2:
            tmp.append(lsplit)
    return tmp

MAFFT_out = "/home/kaihami/Desktop/RR_files/REC_Final_By_domain/REC_FASTA_2/MAFFT_out/MAFFT_Reformated/"

Res_lst = open("/home/kaihami/Desktop/RR_files/MAFFT_Conserved_aa_2.txt").read().split("\n")

Residues_lst = []
save_path = "/home/kaihami/Desktop/RR_files/MAFFT_1_lista/"

for line in Res_lst:
    lsplit = line.split("\t")
    if len(lsplit) >2:
        Residues_lst.append(lsplit)

for ele in Residues_lst:
    File = ele[0]
    B1_D_1 = ele[1]
    B2_D_2 = ele[2]
    B3_D_Phos = ele[3]
    B4_end_S_T = ele[4]
    B5_end_K = ele[5]

    To_Open = MAFFT_out+File+"_reformat.txt"

    MAF_format = open(To_Open).read().split("\n")

    MAFFT_Final = []
    for line in MAF_format:
        lsplit = line.split(",")
        if len(lsplit) >2:
            MAFFT_Final.append(lsplit)
    for line in MAFFT_Final:
        tmp = []
        locus = line[0]
        seq = line[1]
        file2 = line[2]
        try:
            AA_B1 = seq[int(B1_D_1)-1]
        except:
            AA_B1 = "Error"
            print "Error", locus,
        try:
            AA_B2 = seq[int(B2_D_2)-1]
        except:
            AA_B2 = "Error"
            print "Error2", locus
        try:
            AA_B3 = seq[int(B3_D_Phos)-1]

        except:
            AA_B3 = "Error"
            print "Error3", locus
        try:
            AA_B4 = seq[int(B4_end_S_T)-1]
        except:
            AA_B4 = "Error"
            print "Error4", locus
        try:
            AA_B5 = seq[int(B5_end_K)-1]
        except:
            AA_B5 = "Error"
            print "Error5", locus, file2
        tmp.extend((locus, seq, B1_D_1, B2_D_2, B3_D_Phos, B4_end_S_T, B5_end_K, AA_B1, AA_B2, AA_B3, AA_B4, AA_B5 ))
        with open(save_path + file2 + "_AA.txt", "a") as f:
            for pos in xrange(0, len(tmp)):
                if pos != (len(tmp)-1):
                    f.write(tmp[pos])
                    f.write(",")
                else:
                    f.write(tmp[pos])
            f.write("\n")
