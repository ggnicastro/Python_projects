__author__ = 'kaihami'
import os

#os.system("/home/kaihami/FastQC/fastqc --extract --outdir " +current_dir + " " + os.path.join(current_dir, fastq))
def fastQC(read_path,output_path):
    """
    Read Quality Control
    Input: Read, and outpath path
    """
    os.system('./FastQC/fastqc --extract --outdir ' + output_path + " " + read_path)

#os.system("fastq_quality_filter -q 28 -p 75 -o "+name_final+ " -i "+os.path.join(current_dir, fastq) + " -v")

def Trim(read_path, read_name, output_path):
    """
    FastX toolkit
    """
    name_final = "trimmed_"+read_name #output file name
    output = output_path+name_final
    os.system("fastq_quality_filter -q 28 -p 75 -o "+ output + " -i "+ read_path + " -v")


def Edge_call(Reference_genome, ptt, rnt, R1_file, R2_file, OUTPUT_PATH, M = "500"):
    os.system("/home/kaihami/EDGE_pro_v1.3.1/edge.pl -g " + Reference_genome +
              " -p "+ ptt +
              " -r " + rnt +
              " -u " + R1_file +
              " -v " + R2_file +
              " -M " + M
              + " -o " + OUTPUT_PATH)
    print "Finish"


#reads /home/kaihami/Desktop/Xanthomonas/SRR586023_1.fastq
sample_1_1 = "/home/kaihami/Desktop/Xanthomonas/SRR586023_1.fastq"
sample_1_2 = "/home/kaihami/Desktop/Xanthomonas/SRR586023_2.fastq"
sample_1_1_trim = "/home/kaihami/Desktop/Xanthomonas/trimmed_SRR586023_1.fastq"
sample_1_2_trim = "/home/kaihami/Desktop/Xanthomonas/trimmed_SRR586023_2.fastq"

#Analysis quality
fastQC(sample_1_1, "/home/kaihami/Desktop/Xanthomonas/")
fastQC(sample_1_2, "/home/kaihami/Desktop/Xanthomonas/")

Trim(sample_1_1, "SRR586023_1", "/home/kaihami/Desktop/Xanthomonas/")
Trim(sample_1_2, "SRR586023_2", "/home/kaihami/Desktop/Xanthomonas/")

Main_dir = "/home/kaihami/Desktop/RNA-Seq/"
reference_genome = Main_dir+ "Reference/Xanthomonas.fa"
ptt = Main_dir + "Reference/Xanthomonas.ptt"
rnt = Main_dir + "Reference/Xanthomonas.rnt"
output_path = Main_dir + "EDGE-Pro/"
#Reference_genome, ptt, rnt, R1_file, R2_file, OUTPUT_PATH, M = "500"
Edge_call(reference_genome, ptt,rnt, sample_1_1_trim, sample_1_2_trim, output_path)