__author__ = 'kaihami'
#/home/kaihami/Desktop/ALR_filogenia/All_bacteria_faa_150116/DBs/
import os
di = "/home/kaihami/Desktop/ALR_filogenia/All_bacteria_faa_150116/DBs/"

def NCBI_DB(path_in, path_out):
    os.system("makeblastdb -in "+path_in+" -parse_seqids -dbtype 'prot' -out "+path_out)
    print "Done"

for fi in os.listdir(di):
    fasta_seq = os.path.join(di, fi)
    uid = fi.split("_")[-1]
    for fasta_file in os.listdir(fasta_seq):
        fasta_path = os.path.join(fasta_seq, fasta_file)
        print fasta_path
        path_out = "/home/kaihami/Desktop/ALR_filogenia/All_bacteria_faa_150116/NCBI_DB/"+fi+"/"+uid
        os.mkdir("/home/kaihami/Desktop/ALR_filogenia/All_bacteria_faa_150116/NCBI_DB/"+fi)
        NCBI_DB(fasta_path, path_out)
print "Finish"