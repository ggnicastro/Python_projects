__author__ = 'kaihami'

#Usar primeiro, depois
#BioPython_Result_handle
#e depois
#BioPython_Find_Fasta_by_uid


from Bio.Blast.Applications import NcbiblastpCommandline
import os
def BLAST(q, DB, output):
    blastx_cline = NcbiblastpCommandline(query=q, db=DB, evalue=0.001, outfmt=5, out=output)
    stdout, stderr = blastx_cline()

gene = "/home/kaihami/Desktop/ALR_filogenia/NasB/NasB.faa"

Dbs = "/home/kaihami/Desktop/ALR_filogenia/All_bacteria_faa_150116/NCBI_DB/"
x=0
for data in os.listdir(Dbs):
    uid = data.split("_")[-1]
    for db in os.listdir(Dbs+data):
        if db.endswith(".phr"):
            database = db.split(".")[0]
            database_path = os.path.join(Dbs, data, database)
            output_dir = "/home/kaihami/Desktop/ALR_filogenia/NasB/"+data+"/"
            output = "/home/kaihami/Desktop/ALR_filogenia/NasB/"+data+"/"+uid+".xml"
            os.mkdir(output_dir)
            print 'gene', gene
            BLAST(gene, database_path, output)
            x+=1
            print str(len(os.listdir(Dbs))-x)

            #os.system("blastp -query "+gene+ " -db "+ database_path+" -out "+ output+" -evalue 0.001 -outfmt 5")
            #blastx -query opuntia.fasta -db nr -out opuntia.xml -evalue 0.001 -outfmt 5
            #blastp -query Nar.faa -db Pseudomonas_aeruginosa_PA14 -out Test.xml -evalue 0.001 -outfmt 5
print "Finish"
print """
   /) /)
  ( ^.^ )
 C(") (")
"""