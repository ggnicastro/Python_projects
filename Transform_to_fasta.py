__author__ = 'kaihami'

""" take the RR_fasta_xx_formated and output a fasta file with a >uID and the sequence \n\n"""

to_open = "/home/kaihami/Desktop/Python/RR_Bioinfo/Seq_RR/RR_format/Merge_Genome_ID/Fasta/Fasta_formatted/Complete/RR_fasta_others_formated2"

fi = open(to_open, "r").read().split("\n")
total =[]
for line in fi:
    if len(line.split(",")) >2:
        total.append(line.split(","))
del total[0]
save_path = "/home/kaihami/Desktop/Python/RR_Bioinfo/Seq_RR/RR_format/Merge_Genome_ID/Fasta/Fasta_formatted/Complete/Others_fasta.txt"

for ele in total:
    uid = ele[-2]
    fasta = ele[-1]
    with open(save_path, 'a') as f:
        f.write(">")
        f.write(str(uid))
        f.write("\n")
        f.write(str(fasta))
        f.write("\n")
        f.write("\n")
conf = "/home/kaihami/Desktop/Python/RR_Bioinfo/Seq_RR/RR_format/Merge_Genome_ID/Fasta/Fasta_formatted/Complete/Others_fasta.txt"
fi2 = open(conf, "r").read().split("\n")
x=0
for line in fi2:
    if ">" in line:
        x +=1
if x == len(total):
    print "Fine"