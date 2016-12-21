__author__ = 'kaihami'
"""
Generate a quality html file of pre trim and after trim (with fastqc)
trim samples quality phred score 28 percentage 75%
TODO: Good for iBRA
"""
import os
current_dir = "/home/kaihami/Desktop/Analise_geral/"
os.chdir(current_dir)

#Quality control before trim with FastQC
files_list = []
for f in os.listdir(current_dir):
    if f.endswith("fastq"):
        files_list.append(f)

for fastq in files_list:
    os.system("/home/kaihami/FastQC/fastqc --extract --outdir " +current_dir + " " + os.path.join(current_dir, fastq))

#Trim with FastX quality = 32
for fastq in files_list:
    name = fastq.split("_")[0]
    name_final = name+"_trimmed.fastq"
    os.system("fastq_quality_filter -q 28 -p 75 -o "+name_final+ " -i "+os.path.join(current_dir, fastq) + " -v")

#quality after trim
fastq_trim = []

for f_t in os.listdir(current_dir):
    if "trimmed" in f_t:
        fastq_trim.append(f_t)
for fastq in fastq_trim:
    os.system("/home/kaihami/FastQC/fastqc --oudir " +current_dir + " " + os.path.join(current_dir, fastq))

#./fastqc --extract --outdir /home/kaihami/Desktop/Analise_geral/ /home/kaihami/Desktop/Analise_geral/SRR2174566_1.fastq