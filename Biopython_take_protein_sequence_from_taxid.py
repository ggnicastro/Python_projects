__author__ = 'kaihami'

from Bio.Blast import NCBIXML
from Bio import Entrez, SeqIO
import time
import datetime
from Bio import Entrez
from urllib2 import HTTPError

entrezDbName = 'protein'
Entrez.email = 'kaihami@gmail.com'

fi = open("/home/kaihami/Desktop/Python/RR_Bioinfo/Seq_protein_genome/tax_id", "r").read().split("\n")
taxon = []
start_time = time.time()
start_time2 = time.time()

for line in fi:
    a = line.lstrip()
    if len(str(a)) >5:
        taxon.append(a)
len(taxon)
separator = ","
for tax in taxon:
    x = 0
    y = 0
    total_time = []
    entrezQuery = "txid%s[organism]"%(tax)
    searchResultHandle = Entrez.esearch(db=entrezDbName, term=entrezQuery, retmax = 100000)
    searchResult = Entrez.read(searchResultHandle)
    searchResultHandle.close()

    x +=1

    # Get the data.
    uidList = searchResult['IdList']

    for i in uidList:
        try:
            entryData = Entrez.efetch(db=entrezDbName, id=i, rettype='fasta').read()
            x = Entrez.efetch(db=entrezDbName, id = i, retmode = "xml")
        except HTTPError:
            time.sleep(20)
            entryData = Entrez.efetch(db=entrezDbName, id=i, rettype='fasta').read()
            x = Entrez.efetch(db=entrezDbName, id = i, retmode = "xml")

        y +=1

        records = Entrez.read(x)
        organism_name = records[0]["GBSeq_organism"]
        with open("/home/kaihami/Desktop/Python/RR_Bioinfo/Seq_protein_genome/"+tax+".txt", 'a') as f:
            f.write(entryData)
            f.close()
        time.sleep(1.5)
        end_time = time.time()
        time_elapsed = end_time - start_time

        print "*"*40
        print "Genes left" + str((len(uidList)-y))
        print "*"*40
        print "Time per gene " + str(datetime.timedelta(seconds=time_elapsed))

        total_time.append(time_elapsed)
        start_time = end_time

    with open("/home/kaihami/Desktop/Python/RR_Bioinfo/Seq_protein_genome/elapsed_time_gene.txt", 'a') as f2:
        tmp = []
        avg = sum(total_time)/float(len(total_time))
        f2.write(tax+",")
        f2.append(avg+",")
        f2.append(str(min(total_time)+","))
        f2.append(str(max(total_time)))

    end_time2 = time.time()
    time_elapsed2 = end_time2 - start_time2
    print "*"*40
    print "Taxon left" + str((len(taxon)-x))
    print "*"*40
    print "Time per taxon " + str(datetime.timedelta(seconds=time_elapsed2))
    star_time2 = end_time2