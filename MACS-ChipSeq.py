__author__ = 'kaihami'
import os

"""Read SRA and convert to Fastq file"""

fastq = "/home/kaihami/sratoolkit.2.4.4-ubuntu64/bin/fastq-dump "
file_path = "/home/kaihami/Desktop/SigX/"
Sample1 = "SRA_Chip_SigX_H1.sra "
Sample2 = "SRA_Chip_SigX_H2.sra "
Sample3 = "SRA_Chip_Control_H1.sra "
Sample4 = "SRA_Chip_Control_H2.sra "
Sample5 = "SRA_Chip_Control_unknown1.sra "
Sample6 = "SRA_Chip_Control_unknown2.sra "
Sample7 = "SRA_Chip_SigX_unknown1.sra "
Sample8 = "SRA_Chip_SigX_unknown2.sra "

os.system(fastq + file_path+Sample1 + " -O "+ file_path)
os.system(fastq + file_path+Sample2+ " -O "+ file_path)
os.system(fastq + file_path+Sample3+ " -O "+ file_path)
os.system(fastq + file_path+Sample4+ " -O "+ file_path)
os.system(fastq + file_path+Sample5+ " -O "+ file_path)
os.system(fastq + file_path+Sample6+ " -O "+ file_path)
os.system(fastq + file_path+Sample7+ " -O "+ file_path)
os.system(fastq + file_path+Sample8+ " -O "+ file_path)

#Sort the sam files
sam_files_path = "/home/kaihami/Desktop/SigX/Chip-Seq/"
sample1_sam_unsorted = sam_files_path + "Control_H1.alignments"
sample2_sam_unsorted = sam_files_path + "Control_H2.alignments"
sample3_sam_unsorted = sam_files_path + "SigX1_H1.alignments"
sample4_sam_unsorted = sam_files_path + "SigX_H2.alignments"
sample5_sam_unsorted = sam_files_path + "Control_unknown1.alignments"
sample6_sam_unsorted = sam_files_path + "Control_unknown2.alignments"
sample7_sam_unsorted = sam_files_path + "SigX_unknown1.alignments"
sample8_sam_unsorted = sam_files_path + "SigX_unknown2.alignments"

Picard_path = "/home/kaihami/picard-tools-1.119/"
os.system("java -Xmx2g -jar " + Picard_path + "SortSam.jar " + "INPUT= " + sample1_sam_unsorted  + " OUTPUT= " +
          sam_files_path + "sorted_" + "Control_H1" + ".sam" + " SORT_ORDER=coordinate")

os.system("java -Xmx2g -jar " + Picard_path + "SortSam.jar " + "INPUT= " + sample2_sam_unsorted  + " OUTPUT= " +
          sam_files_path + "sorted_" + "Control_H2" + ".sam" + " SORT_ORDER=coordinate")

os.system("java -Xmx2g -jar " + Picard_path + "SortSam.jar " + "INPUT= " + sample3_sam_unsorted  + " OUTPUT= " +
          sam_files_path + "sorted_" + "SigX_H1" + ".sam" + " SORT_ORDER=coordinate")

os.system("java -Xmx2g -jar " + Picard_path + "SortSam.jar " + "INPUT= " + sample4_sam_unsorted  + " OUTPUT= " +
          sam_files_path + "sorted_" + "SigX_H2" + ".sam" + " SORT_ORDER=coordinate")

os.system("java -Xmx2g -jar " + Picard_path + "SortSam.jar " + "INPUT= " + sample5_sam_unsorted  + " OUTPUT= " +
          sam_files_path + "sorted_" + "Control_unknown1" + ".sam" + " SORT_ORDER=coordinate")

os.system("java -Xmx2g -jar " + Picard_path + "SortSam.jar " + "INPUT= " + sample6_sam_unsorted  + " OUTPUT= " +
          sam_files_path + "sorted_" + "Control_unknown2" + ".sam" + " SORT_ORDER=coordinate")
os.system("java -Xmx2g -jar " + Picard_path + "SortSam.jar " + "INPUT= " + sample7_sam_unsorted  + " OUTPUT= " +
          sam_files_path + "sorted_" + "SigX_unknown1" + ".sam" + " SORT_ORDER=coordinate")
os.system("java -Xmx2g -jar " + Picard_path + "SortSam.jar " + "INPUT= " + sample8_sam_unsorted  + " OUTPUT= " +
          sam_files_path + "sorted_" + "SigX_unknown2" + ".sam" + " SORT_ORDER=coordinate")

#Regular peak
#macs2 callpeak -t  -c  -f  -g  -n  -B -q
#-t <treatment>
#-c <Control>
#-f format file (e.g. sam)
#-g genome size
#-n Output file name
#-B
#-q FDR (0.01)
#--outdir Save in this dir
sam_files_path = "/home/kaihami/Desktop/SigX/Chip-Seq/"
SigX_H1 = sam_files_path + "sorted_SigX_H1.sam"
SigX_H2 = sam_files_path + "sorted_SigX_H2.sam"
Control1 = sam_files_path + "sorted_Control_H1.sam"
Control2 = sam_files_path + "sorted_Control_H2.sam"
SigX_unk1 = sam_files_path + "sorted_SigX_unknown1.sam"
SigX_unk2 = sam_files_path + "sorted_SigX_unknown2.sam"
Control_unk1 = sam_files_path + "sorted_Control_unknown1.sam"
Control_unk2 = sam_files_path + "sorted_Control_unknown2.sam"

"macs2 callpeak -t " + SigX_H1 + " -c " + Control1 + " -f sam -g 6537648 -n Chip-Seq_H1 -B -q 0.01 --outdir /home/kaihami/Desktop/SigX/Chip-Seq/MACS2"

os.system("macs2 callpeak -t " + SigX_H2 + " -c " + Control2 + " -f SAM --nomodel -g 6537648 -n Chip-Seq_H2 -B -q 0.01 --outdir /home/kaihami/Desktop/SigX/Chip-Seq/MACS2")

os.system("macs2 callpeak -t " + SigX_H1 + " "+ SigX_H2 + " -c " + Control1 + " " + Control2 + " -f SAM -g 6537648 -n Chip-Seq_H1a2 -B -q 0.01 --outdir /home/kaihami/Desktop/SigX/Chip-Seq/MACS2")

os.system("macs2 callpeak -t " + SigX_unk1 + " -c " + Control_unk1 + " -f SAM --nomodel -g 6537648 -n Chip-Seq_unk1 -B -q 0.01 --outdir /home/kaihami/Desktop/SigX/Chip-Seq/MACS2")

os.system("macs2 callpeak -t " + SigX_unk2 + " -c " + Control_unk2 + " -f SAM --nomodel -g 6537648 -n Chip-Seq_unk2 -B -q 0.01 --outdir /home/kaihami/Desktop/SigX/Chip-Seq/MACS2")

os.system("macs2 callpeak -t " + SigX_unk1 + " " + SigX_unk2 + " -c " + Control_unk1 +" " + Control_unk2+ " -f SAM --nomodel -g 6537648 -n Chip-Seq_unk1a2 -B -q 0.01 --outdir /home/kaihami/Desktop/SigX/Chip-Seq/MACS2")

os.system("macs2 callpeak -t " + SigX_unk1 + " " + SigX_unk2 + " "+ SigX_H1 + " " + SigX_H2 + " -c " + Control_unk1 +" " + Control_unk2 + " " + Control1 + " " + Control2 + " -f SAM --nomodel -g 6537648 -n Chip-Seq_All -B -q 0.01 --outdir /home/kaihami/Desktop/SigX/Chip-Seq/MACS2")

