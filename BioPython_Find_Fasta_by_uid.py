__author__ = 'kaihami'
import os

def get_seq(gene,DB_file):
    seq = ""
    for x in xrange(0, len(DB_file)):
        if gene in DB_file[x]:
            for y in xrange(x+1, len(DB_file)):
                if ">" in DB_file[y]:
                   break
                else:
                    seq += DB_file[y]
    return seq

query = open('/home/kaihami/Desktop/ALR_filogenia/Results_alignment_all_bacs/NasB.txt', "r").read().split("\n")

query_ls = []

for line in query:
    a = line.split("\t")
    if len(a)>2:
        query_ls.append(a)
DB_path = "/home/kaihami/Desktop/ALR_filogenia/All_bacteria_faa_150116/DBs/"
y= 0
head = ["gene",
        "uid",
        "aa_identity",
        "percentage_identity",
        "gene_result",
        "fasta_AA"]
#write head
with open("/home/kaihami/Desktop/ALR_filogenia/Results_alignment_all_bacs/NasB_with_fasta.txt", "a") as f:
    f.write("\t".join(head))
    f.write("\n")
for line in query_ls:
    gene = line[0]
    uid = line[1]
    aa_identity = line[2]
    percentage_identity = line[3]
    gene_result = line[-1]
    tmp = []
    for d in os.listdir(DB_path):
        uid_file = d.split("_")[-1]
        if uid == uid_file:
            for fi in os.listdir(os.path.join(DB_path, d)):
                DB_file = open(os.path.join(DB_path, d, fi), "r").read().split("\n")
                del DB_file[-1]
                seq =get_seq(gene_result, DB_file)
                features = [gene, uid, aa_identity, percentage_identity, gene_result, seq]
                with open("/home/kaihami/Desktop/ALR_filogenia/Results_alignment_all_bacs/NasB_with_fasta.txt", "a") as f:
                    f.write("\t".join(features))
                    f.write("\n")
print "Done"

