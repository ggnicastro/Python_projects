import os

os.system ("/home/kaihami/cufflinks-2.2.1.Linux_x86_64/cufflinks -o /home/kaihami/Desktop/PA14_1analise/Cufflinks/PA14_pJN105_1 --GTF /home/kaihami/Desktop/PA14_1analise/Reference/Pseudomonas_new.gff3 --no-update /home/kaihami/Desktop/PA14_1analise/TopHat/PA14_pJN105_1/accepted_hits.bam")
os.system ("/home/kaihami/cufflinks-2.2.1.Linux_x86_64/cufflinks -o /home/kaihami/Desktop/PA14_1analise/Cufflinks/PA14_26570_1 --GTF /home/kaihami/Desktop/PA14_1analise/Reference/Pseudomonas_new.gff3 --no-update /home/kaihami/Desktop/PA14_1analise/TopHat/PA14_26570_1/accepted_hits.bam")
os.system ("/home/kaihami/cufflinks-2.2.1.Linux_x86_64/cufflinks -o /home/kaihami/Desktop/PA14_1analise/Cufflinks/PA14_21550_1 --GTF /home/kaihami/Desktop/PA14_1analise/Reference/Pseudomonas_new.gff3 --no-update /home/kaihami/Desktop/PA14_1analise/TopHat/PA14_21550_1/accepted_hits.bam")

./gffread -E /home/kaihami/Desktop/PA14_1analise/Reference/Pseudomonas.gff -o /home/kaihami/Desktop/Pseudomonas_new.gff
