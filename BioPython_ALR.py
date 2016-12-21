__author__ = 'kaihami'
#construct DB

#/home/kaihami/Desktop/ALR_filogenia/All_bacteria_faa_150116/
import os

def join_fasta(seq_ls, bac_folder):
    all_seq = []
    for seq in seq_ls:
        fasta_seq = os.path.join(bac_folder, seq)
        fasta_read = open(fasta_seq,"r").read().split("\n")
        for line in fasta_read:
            if len(line) >2:
                all_seq.append(line)
    return all_seq



bac_fasta = "/home/kaihami/Desktop/ALR_filogenia/All_bacteria_faa_150116/all/"

os.listdir(bac_fasta)
for folder in os.listdir(bac_fasta):
    bac_folder = os.path.join(bac_fasta, folder)
    seq_ls = []
    for seq in os.listdir(bac_folder):
        seq_ls.append(seq)
    # join fasta
    fastas = join_fasta(seq_ls, bac_folder)
    os.mkdir("/home/kaihami/Desktop/ALR_filogenia/All_bacteria_faa_150116/DBs/"+folder)
    bac_db_dir = "/home/kaihami/Desktop/ALR_filogenia/All_bacteria_faa_150116/DBs/"+folder
    for line in fastas:
        with open(bac_db_dir+"/"+folder+".faa", "a") as f:
            f.write(line)
            f.write("\n")
    print bac_db_dir
print "Finish"