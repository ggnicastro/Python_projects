__author__ = 'kaihami'

#Handle BLAST result
from Bio.Blast import NCBIXML
import os
def find_homolog(result, gene_len, uid,save_file, query):
    ls = []
    result_handle = open(result)

    blast_records = NCBIXML.parse(result_handle)
    blast_record = next(blast_records)
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            identity = float(hsp.identities)/float(len(gene_len))
            identity_percentage = identity*100.0
            tmp = []
            if identity_percentage >20:

                #print "Identity percentage: " + "%.2f" % (identity_percentage)
                #print hsp.identities #AA identical
                #% identical
                #print float(hsp.identities)/float(len(seq))
                #print "Result: ", alignment.title #result
                tmp = [query, uid, str(hsp.identities), str(identity_percentage), alignment.title]
            print tmp
            if len(tmp) >2:
                with open(save_file, "a") as f:
                    f.write("\t".join(tmp))
                    f.write("\n")


    return ls
###
#gene, uid(get from bac), identity (aa),%identity (identity_percentage),result_gene
###
gene = open("/home/kaihami/Desktop/ALR_filogenia/NasB/NasB.faa", "r").read().split("\n")
seq = ""
for line in gene:
    if not line.startswith(">") and len(line) >2:
        seq += line
###

bacs = "/home/kaihami/Desktop/ALR_filogenia/NasA/"
save_path = "/home/kaihami/Desktop/ALR_filogenia/Results_alignment_all_bacs/NasB.txt"
for bac in os.listdir(bacs):
    if os.path.isdir(os.path.join(bacs,bac)):
        path_bac = os.path.join(bacs, bac)
        print bac
        uid = bac.split("_")[-1]
        for xm in os.listdir(path_bac):
            tmp = find_homolog(os.path.join(path_bac, xm), seq,uid, save_path, "NasB")
            print tmp
            #if len(tmp) == 0:
                #print path_bac
print "Finish"