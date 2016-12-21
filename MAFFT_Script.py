__author__ = 'kaihami'
import os
dir = "/home/kaihami/Desktop/RR_files/REC_Final_By_domain/REC_FASTA_2/FASTA_50_bucket/"
REC_file_lst = []

for File in os.listdir(dir):
    if File.endswith(".txt"):
        REC_file_lst.append(File)
x = 0
for ele in REC_file_lst:
    x+= 1
    path = ele
    INP = dir+path
    part = path.split(".")[0]
    OUT = "/home/kaihami/Desktop/RR_files/REC_Final_By_domain/REC_FASTA_2/MAFFT_out/MAFFT_" + part
    a = os.system("mafft --localpair --maxiterate 1000 --preservecase " + INP + " > " + OUT)
    print "*"*50
    print x
    print "*"*50

INP = "/home/kaihami/Desktop/RR_files/REC_Final_By_domain/REC_FASTA_2/FASTA_50_bucket/FASTA_non_align.txt"
OUT = "/home/kaihami/Desktop/RR_files/REC_Final_By_domain/REC_FASTA_2/MAFFT_out/MAFFT_FASTA_non_align.txt"
a = os.system("mafft --localpair --maxiterate 1000 --preservecase " + INP + " > " + OUT)