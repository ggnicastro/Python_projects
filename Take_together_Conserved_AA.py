__author__ = 'kaihami'
"""
From this file: MAFFT_FASTA_CheVfamily-CheW-REC_1_AA.txt
Merge all Files, and add a column with the original File name
Output : MAFFT_FASTA_All.txt (locus, MAFFT_align, B1_D1, B2_D2, B3_D_phos, B4_S/T, B5_K,
         AA_D1, AA_D2, AA_D3, AA_S/T, AA_K, File_name
"""
import os
File_dir = "/home/kaihami/Desktop/RR_files/MAFFT_1_lista/With_Conserved_AA/"
save_path = "/home/kaihami/Desktop/RR_files/MAFFT_1_lista/Separated_by_conservation/ALR/"
save_path_con = "/home/kaihami/Desktop/RR_files/MAFFT_1_lista/Separated_by_conservation/Conserverd_D/"
Lst_File = []
for File in os.listdir(File_dir):
    if File.endswith(".txt"):
        Lst_File.append(File)

for fi in Lst_File:
    Open = File_dir+fi
    Open_file = open(Open, "r").read().split("\n")
    total = []
    for line in Open_file:
        lsplit = line.split(",")
        if len(lsplit) > 2:
            total.append(lsplit)
    for ele in total:
        tmp = []
        locus = ele[0]
        Seq = ele[1]
        B1_D1 = ele[2]
        B2_D2 = ele[3]
        B3_D_phos = ele[4]
        B4_S_T = ele[5]
        B5_K = ele [6]
        AA_B1 = ele[7]
        AA_B2 = ele[8]
        AA_B3 = ele[9]
        AA_B4 = ele[10]
        AA_B5 = ele[11]
        order = AA_B1 + AA_B2 + AA_B3 + AA_B4 + AA_B5
        tmp.extend((locus, Seq, B1_D1, B2_D2, B3_D_phos, B4_S_T, B5_K, AA_B1, AA_B2, AA_B3, AA_B4, AA_B5, order, fi))
        if "D".lower() == AA_B3.lower():
            with open(save_path_con + order+".txt", "a") as f:
                for pos in xrange(0, len(tmp)):
                    if pos != (len(tmp)-1):
                        f.write(tmp[pos])
                        f.write(",")
                    else:
                        f.write(tmp[pos])
                f.write("\n")
        else:
            with open(save_path + order+".txt", "a") as f:
                for pos in xrange(0, len(tmp)):
                    if pos != (len(tmp)-1):
                        f.write(tmp[pos])
                        f.write(",")
                    else:
                        f.write(tmp[pos])
                f.write("\n")
