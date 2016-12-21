__author__ = 'kaihami'

"""
From a Locus_tag find the protein using BioPython
"""

from Bio.Blast import NCBIXML
from Bio import Entrez, SeqIO
from urllib2 import HTTPError
import time
import datetime

total_time = []
entrezDbName = 'protein'
Entrez.email = 'kaihami@gmail.com'

rr_file = open("/home/kaihami/Desktop/Python/RR_Bioinfo/Seq_RR/RR_format/Merge_Genome_ID/Continue", "r").read().split("\n")
rr = []
for line in rr_file:
    a = line.split("\t")
    tmp =[]
    for x in xrange(0,8):
        try:
            tmp.append(a[x])
        except:
            pass
    if len(tmp) > 2:
        rr.append(tmp)

#file
take = "Archaea"
save_path = "/home/kaihami/Desktop/Python/RR_Bioinfo/Seq_RR/RR_format/Merge_Genome_ID/Fasta/Deps_continue"

with open(save_path, 'a') as f:
    f.write("Taxonomy,Bacteria,Bacteria2,Phylum,Genome_ID,CDS,RR_class,Locus_tag,UID_number,Fasta_header,Fasta_Sequence")
    f.write("\n")

with open("/home/kaihami/Desktop/Python/RR_Bioinfo/Seq_RR/RR_format/Merge_Genome_ID/Fasta/elapsed_time_gene.txt", 'a') as f2:
    f2.write("Phylum,")
    f2.write("Average,")
    f2.write("Min,")
    f2.write("Max,")
    f2.write("Total_time,Total_seq")
    f2.write("\n")

start_time = time.time()
y = 0
for y in xrange(0, len(rr)):
    tax = rr[y][0]
    bac = rr[y][1]
    bac2 = rr[y][2]
    phylum = rr[y][3]
    gen_id = rr[y][4]
    CDS = rr[y][5]
    rr_fun = rr[y][6]
    locus_tag = rr[y][7]
    if len(locus_tag) >1:
        locus_format = locus_tag.replace("#","").replace("*","")

        searchResultHandle = Entrez.esearch(db=entrezDbName, term=locus_format, retmax = 1)
        searchResult = Entrez.read(searchResultHandle)
        searchResultHandle.close()
        uidList = searchResult['IdList']
        uidString = str(uidList).replace("[","").replace("]","").replace("'","")

        for i in uidList:
            try:
                entryData = Entrez.efetch(db=entrezDbName, id=i, rettype='fasta').read()
                x = Entrez.efetch(db=entrezDbName, id = i, retmode = "xml")
            except HTTPError:
                try:
                    time.sleep(20)
                    entryData = Entrez.efetch(db=entrezDbName, id=i, rettype='fasta').read()
                    x = Entrez.efetch(db=entrezDbName, id = i, retmode = "xml")
                except HTTPError:
                    time.sleep(60)
                    entryData = Entrez.efetch(db=entrezDbName, id=i, rettype='fasta').read()
                    x = Entrez.efetch(db=entrezDbName, id = i, retmode = "xml")
            fasta_unformat = entryData.split("\n",1)

            fasta_header = fasta_unformat[0].replace(",","")
            fasta_sequence = fasta_unformat[1].replace("\n","")
            tmp = []
            tmp.extend((tax,bac,bac2,phylum,gen_id,CDS,rr_fun,locus_tag,uidString,fasta_header, fasta_sequence))
            with open(save_path, 'a') as f:
                for pos in xrange(0, len(tmp)):
                    if pos != (len(tmp)-1):
                        f.write(tmp[pos])
                        f.write(",")
                    else:
                        f.write(tmp[pos])
                f.write("\n")
            time.sleep(2)
            end_time = time.time()
            time_elapsed = end_time - start_time
            y+=1
            print "*"*40
            print "Genes left " + str((len(rr)-y))
            print "*"*40
            print "Time per gene " + str(datetime.timedelta(seconds=time_elapsed))

            total_time.append(time_elapsed)
            start_time = end_time


