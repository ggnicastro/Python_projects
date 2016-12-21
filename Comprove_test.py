__author__ = 'kaihami'

import os

Dir1 = "/home/kaihami/Desktop/RR_files/REC_Final_By_domain/REC_FASTA_2/FASTA_50_bucket/"

FASTA = []
for File in os.listdir(Dir1):
    if File.endswith(".txt"):
        FASTA.append(File)

FASTA_format = []

for line in FASTA:
    a = line.replace("FASTA_","").replace(".txt", "")
    FASTA_format.append(a)

Dir2 = "/home/kaihami/Desktop/RR_files/REC_Final_By_domain/REC_FASTA_2/MAFFT_out/"

Total = []

for File2 in os.listdir(Dir2):
    if File2.startswith("MAFFT"):
        Total.append(File2)
Total_format = []
for ele in Total:
    a = ele.replace("MAFFT_", "").replace("FASTA_","")
    Total_format.append(a)

dup2 = []
dup = []

for ele in FASTA_format:
    if ele not in Total_format:
        dup.append(ele)
    if ele in Total_format:
        dup2.append(ele)