__author__ = 'kaihami'
"""
Get sRNA from:
    "The Single-Nucleotide Resolution Transcriptome of Pseudomonas aeruginosa Grown in Body Temperature"
and
    "The Pseudomonas aeruginosa Transcriptome in Planktonic Cultures and Static Biofilms Using RNA Sequencing"

and put it in .rnt file (rRNA and tRNA)
"""
import os

hausler_sRNA = open("/home/kaihami/Desktop/RNA-Seq/sRNAs/Hausler_sRNA.txt").read().split("\n")
h_sRNA_list = []

for line in hausler_sRNA:
    if len(line.split("\t")) >1:
        h_sRNA_list.append(line.split("\t"))
#h_sRNA_list: [0]: Name, [1] start, [2] end, [3] strand, [4] gene context, [5] start, [6] end, [7] strand
#             4, 5, 6, 7 => PA14, 1, 2, 3 => PA01
h_sRNA_list_final = []

for line in h_sRNA_list:
    if "Namea" not in line and "" != line[0]:
        h_sRNA_list_final.append([line[0], line[5], line[6], line[7], line[8]])
        #name, gene context, start, end, strand in PA14
#write file
with open("/home/kaihami/Desktop/RNA-Seq/sRNAs/Hausler_sRNA_format.txt", "a") as f:
    f.write("name\tgene context\tstart\tend\tstrand\n")
for line in h_sRNA_list_final:
    with open("/home/kaihami/Desktop/RNA-Seq/sRNAs/Hausler_sRNA_format.txt", "a") as f:
        to_write = "\t".join(line)
        f.write(to_write)
        f.write("\n")

###
Lory_sRNA = open("/home/kaihami/Desktop/RNA-Seq/sRNAs/Lory_sRNA.txt", 'r').read().split("\n")
Lory_list = []
for line in Lory_sRNA:
    if "Id" not in line and len(line.split("\t")) >2:
        Lory_list.append(line.split("\t"))
info = Lory_sRNA[0].split("\t")
infos = [info[0], info[1], info[2],info[3]]

Lory_list_final = []
for line in Lory_list:
    Lory_list_final.append([line[0],line[1],line[2],line[3]])
with open("/home/kaihami/Desktop/RNA-Seq/sRNAs/Lory_sRNA_format.txt", "a") as f:
    f.write("\t".join(infos))
    f.write("\n")
for line in Lory_list_final:
    with open("/home/kaihami/Desktop/RNA-Seq/sRNAs/Lory_sRNA_format.txt", "a") as f:
        to_write = "\t".join(line)
        f.write(to_write)
        f.write("\n")

#Compare Hausler and Lory
Hausler_format = open("/home/kaihami/Desktop/RNA-Seq/sRNAs/Hausler_sRNA_format.txt","r").read().split("\n")
len(Hausler_format)
Lory_format = open("/home/kaihami/Desktop/RNA-Seq/sRNAs/Lory_sRNA_format.txt",'r').read().split("\n")
len(Lory_format)
hausler_list_format = []
for line in Hausler_format:
    if "name" not in line and len(line.split("\t"))>2:
        hausler_list_format.append(line.split("\t"))
lory_list_format = []
for line in Lory_format:
    if "Id" not in line and len(line.split("\t"))>2:
        lory_list_format.append(line.split("\t"))

sRNA_dic = {}
for line in hausler_list_format:
    name = line[0]
    start = line[2]
    end = line[3]
    strand = line[4]
    sRNA_dic[start] = [name, start, end, strand]
for line2 in lory_list_format:
    start2 = line2[1]
    end2 = line2[2]
    strand2 = line2[3]
    if start2 not in sRNA_dic.keys():
        sRNA_dic[start2] = line2

for key, value in sRNA_dic.items():
    with open('/home/kaihami/Desktop/RNA-Seq/sRNAs/all_sRNA.txt',"a") as f:
        print value
        f.write("\t".join(value))
        f.write("\n")

#put it in rnt File
rnt = open("/home/kaihami/Desktop/RNA-Seq/sRNAs/a.rnt","r").read().split("\n")
rnt_format = []
for x in xrange(1,len(rnt)):
    if len(rnt[x].split("\t"))>2:
        rnt_format.append(rnt[x].split("\t"))
#position [0], strand [1], length [2], PID[3], Gene [4], Synonym [5], code [6], cog [7], Product [8]
rnt_final = []
for ele in rnt_format:
    start, end = ele[0].split("..")
    rnt_final.append([start, end, ele[1],ele[2], ele[3], ele[4], ele[5],ele[6], ele[7], ele[8]])
for l in rnt_final:
    with open('/home/kaihami/Desktop/RNA-Seq/sRNAs/rnt_formated.rnt',"a") as f:
        f.write("\t".join(l))
        f.write("\n")
#open all_sRNA
all_sRNA = open("/home/kaihami/Desktop/RNA-Seq/sRNAs/all_sRNA.txt", "r").read().split("\n")
all_lst = []

for line in all_sRNA:
    if len(line.split("\t"))>2:
        all_lst.append(line.split("\t"))
all_final = []
for line in all_lst:
    start = line[1]
    end = line[2]
    strand = line[3]
    length = int(line[2])-int(line[1])
    force = "116048575"
    put = "-"
    gene = line[0]
    sRNA = "sRNA"
    all_final.append([start,end, strand, str(length), force, "-", gene, "-","-", "sRNA"])

for e in all_final:
    with open('/home/kaihami/Desktop/RNA-Seq/sRNAs/rnt_formated.rnt',"a") as f:
        f.write("\t".join(e))
        f.write("\n")

#format file
rnt_ff = open('/home/kaihami/Desktop/RNA-Seq/sRNAs/rnt_formated.rnt', 'r').read().split("\n")

rnt_ff_l = []

for line in rnt_ff:
    if len(line.split("\t"))>2:
        rnt_ff_l.append(line.split("\t"))

final_file = []
for ele in rnt_ff_l:
    start = ele[0]
    end = ele[1]

    position = start+".."+end
    strand = ele[2]
    lenght = ele[3]
    p = ele[4]
    pp = ele[5]
    gene = ele[6]
    pp2 = ele[7]
    pp3 = ele[8]
    feat = ele[9]
    final_file.append([position, strand, lenght, p, pp, gene, pp2, pp3, feat])

for ff in final_file:
    with open("/home/kaihami/Desktop/RNA-Seq/sRNAs/pseudomonas_050116.txt","a") as f:
        f.write("\t".join(ff))
        f.write("\n")
len(final_file)