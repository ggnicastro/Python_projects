import os
os.system("gunzip /home/kaihami/Desktop/RNA_seq_Raw_files/PA14-pJN105_S1_L001_R2_001.fastq.gz")
os.system("gunzip /home/kaihami/Desktop/RNA_seq_Raw_files/PA14-21550_S2_L001_R1_001.fastq.gz")
os.system("gunzip /home/kaihami/Desktop/RNA_seq_Raw_files/PA14-21550_S2_L001_R2_001.fastq.gz")
os.system("gunzip /home/kaihami/Desktop/RNA_seq_Raw_files/PA14-26570_S3_L001_R2_001.fastq.gz") 
print "Reads sample PA14-pJN105 R1"
os.system("grep "+ "\"@M\"" + "/home/kaihami/Desktop/RNA_seq_Raw_files/PA14-pJN105_S1_L001_R1_001.fastq")
print "Reads sample PA14-pJN105 R2"
os.system("grep "+ "\"@M\"" + "/home/kaihami/Desktop/RNA_seq_Raw_files/PA14-pJN105_S1_L001_R2_001.fastq")
print "Reads sample PA14-21550 R1"
os.system("grep "+ "\"@M\"" + "/home/kaihami/Desktop/RNA_seq_Raw_files/PA14-21550_S2_L001_R1_001.fastq")
print "Reads sample PA14-21550 R2"
os.system("grep "+ "\"@M\"" + "/home/kaihami/Desktop/RNA_seq_Raw_files/PA14-21550_S2_L001_R2_001.fastq")
print "Reads sample PA14-26570 R1"
os.system("grep "+ "\"@M\"" + "/home/kaihami/Desktop/RNA_seq_Raw_files/PA14-26570_S3_L001_R1_001.fastq")
print "Reads sample PA14-26570 R2"
os.system("grep "+ "\"@M\"" + "/home/kaihami/Desktop/RNA_seq_Raw_files/PA14-26570_S3_L001_R2_001.fastq")