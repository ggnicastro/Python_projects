__author__ = 'kaihami'
import os
dir = '/home/kaihami/Desktop/ALR_filogenia/'

fi = open("/home/kaihami/Desktop/ALR_filogenia/ALRs_hitdata(1).txt", "r").read().split("\n")

table = []
for x in xrange(7, len(fi)):
    if len(fi[x].split("\t"))>2:
        table.append(fi[x].split("\t"))
#Query = table[0][0]
#start = table[0][3]
#end = table[0][4]
#acession = table[0][7]
#name = table[0][8]
names_specific = ["LuxR_C_like","HTH_10","HTH_25","HTH_AraC", "HTH_8","HTH_XRE","HTH_ARSR","HTH_CRP","HTH_LUXR",]
names_super = ["HTH_8 superfamily",]
prot_specific = []
prot_super = []
for y in xrange(1, len(table)):
    Que = table[y][0]
    Query = Que.split(">")[-1]
    type = table[y][1]
    start = table[y][3]
    end = table[y][4]
    acession = table[y][7]
    name = table[y][8]
    if type == "specific":
        if name in names_specific:
            prot_specific.append([Query, type, start, end , acession, name])
    if type == "superfamily":
        if "HTH".lower() in name.lower():
            prot_specific.append([Query, type, start, end , acession, name])

for ele in prot_specific:
    with open("/home/kaihami/Desktop/ALR_filogenia/All_HTH_ALRs.txt", "a") as f:
        f.write("\t".join(ele))
        f.write("\n")

no_repeat = []

for ele in prot_specific:
    name = ele[0]
    if name not in no_repeat:
        no_repeat.append(name)
        with open("/home/kaihami/Desktop/ALR_filogenia/no_repeat.txt", "a") as f:
            f.write(name)
            f.write("\n")

no_dir = open("/home/kaihami/Desktop/ALR_filogenia/no_repeat.txt", "r").read().split("\n")
all_info = open("/home/kaihami/Desktop/ALR_filogenia/ALR_protein_strains.txt","r").read().split("\n")
info = []
for line in all_info:
    if len(line.split("\t")) > 2:
        info.append(line.split("\t"))
get_info = []
for ele in no_dir:
    for line in info:
        if ele in line:
            get_info.append(line)
for ele in get_info:
    with open("/home/kaihami/Desktop/ALR_filogenia/ALR_info_HTH_total.txt","a") as f:
        f.write("\t".join(ele))
        f.write("\n")

#get_seq
lux = open("/home/kaihami/Desktop/ALR_filogenia/LuxR/LuxR_ALRs.txt", "r").read().split("\n")

lux_tot = []

for line in lux:
    if len(line.split("\t"))>2:
        lux_tot.append(line.split("\t"))
prot_strain = open("/home/kaihami/Desktop/ALR_filogenia/ALR_protein_strains.txt", "r").read().split("\n")

tot = []

for line in prot_strain:
    if len(line.split("\t"))>2:
        tot.append(line.split("\t"))

Lux_info = []

for line in lux_tot:
    id = line[0]
    type = line[1]
    start = line[2]
    end = line[3]
    domain = line[-1]
    for y in xrange(1,len(tot)):
        entry = tot[y][0]
        status = tot[y][1]
        organism = tot[y][2]
        fasta_tot = tot[y][3]
        if entry == id:
            fasta_par = fasta_tot[int(start):int(end)+1]
            infos = [id, status, organism, str(start),str(end), fasta_tot, fasta_par]
            with open("/home/kaihami/Desktop/ALR_filogenia/LuxR/LuxR_ALR_info.txt", "a") as f:
                f.write("\t".join(infos))
                f.write("\n")

al = open("/home/kaihami/Desktop/ALR_filogenia/LuxR/LuxR_ALR_info.txt", "r").read().split("\n")
p = []
for line in al:
    b = line.split("\t")
    if len(b) >2:
        p.append(b)

for ele in p:
    ID = ele[0]
    fasta = ele[5]
    with open("/home/kaihami/Desktop/ALR_filogenia/LuxR/MAFFT_Lux_ALRs.txt",'a') as f:
        f.write(">")
        f.write(ID)
        f.write("\n")
        f.write(fasta)
        f.write("\n")
        f.write("\n")

import os
INP = "/home/kaihami/Desktop/ALR_filogenia/LuxR/MAFFT_Lux_ALRs.txt"
OUT = "/home/kaihami/Desktop/ALR_filogenia/LuxR/MAFFT_out_Lux_ALR.txt"
a = os.system("mafft --localpair --maxiterate 1000 --preservecase " + INP + " > " + OUT)