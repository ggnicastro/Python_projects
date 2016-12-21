import os
ref_gen_path = "/home/kaihami/Desktop/PA14_1analise/Reference/PA14_reference_genome.fa"
bowtie_output = "/home/kaihami/Desktop/PA14_1analise/Reference/Pseudomonas_reference_genome"
os.system("bowtie2-build " + ref_gen_path + " " + bowtie_output)

os.system("tophat2 -p 1 --mate-std-dev 30 --segment-length 50 -o /home/kaihami/Desktop/PA14_1analise/TopHat2/PA14_pJN105_1 -G /home/kaihami/Desktop/PA14_1analise/Reference/Pseudomonas.gff /home/kaihami/Desktop/PA14_1analise/Reference/Pseudomonas_reference_genome /home/kaihami/Desktop/PA14_1analise/Sequence/trimmed_PA14-pJN105_R1.fastq /home/kaihami/Desktop/PA14_1analise/Sequence/trimmed_PA14-pJN105_R2.fastq")
os.system("tophat2 -p 1 --mate-std-dev 30 --segment-length 50 -o /home/kaihami/Desktop/PA14_1analise/TopHat2/PA14_21550_1 -G /home/kaihami/Desktop/PA14_1analise/Reference/Pseudomonas.gff /home/kaihami/Desktop/PA14_1analise/Reference/Pseudomonas_reference_genome /home/kaihami/Desktop/PA14_1analise/Sequence/trimmed_PA14-21550_R1.fastq /home/kaihami/Desktop/PA14_1analise/Sequence/trimmed_PA14-21550_R2.fastq")
os.system("tophat2 -p 1 --mate-std-dev 30 --segment-length 50 -o /home/kaihami/Desktop/PA14_1analise/TopHat2/PA14_26570_1 -G /home/kaihami/Desktop/PA14_1analise/Reference/Pseudomonas.gff /home/kaihami/Desktop/PA14_1analise/Reference/Pseudomonas_reference_genome /home/kaihami/Desktop/PA14_1analise/Sequence/trimmed_PA14-26570_R1.fastq /home/kaihami/Desktop/PA14_1analise/Sequence/trimmed_PA14-26570_R2.fastq")

os.system ("/home/kaihami/cufflinks-2.2.1.Linux_x86_64/cufflinks -o /home/kaihami/Desktop/PA14_1analise/Cufflinks2/PA14_pJN105_1 --GTF /home/kaihami/Desktop/PA14_1analise/Reference/Pseudomonas.gff --no-update /home/kaihami/Desktop/PA14_1analise/TopHat2/PA14_pJN105_1/accepted_hits.bam")
os.system ("/home/kaihami/cufflinks-2.2.1.Linux_x86_64/cufflinks -o /home/kaihami/Desktop/PA14_1analise/Cufflinks2/PA14_26570_1 --GTF /home/kaihami/Desktop/PA14_1analise/Reference/Pseudomonas.gff --no-update /home/kaihami/Desktop/PA14_1analise/TopHat2/PA14_26570_1/accepted_hits.bam")
os.system ("/home/kaihami/cufflinks-2.2.1.Linux_x86_64/cufflinks -o /home/kaihami/Desktop/PA14_1analise/Cufflinks2/PA14_21550_1 --GTF /home/kaihami/Desktop/PA14_1analise/Reference/Pseudomonas.gff --no-update /home/kaihami/Desktop/PA14_1analise/TopHat2/PA14_21550_1/accepted_hits.bam")
