__author__ = 'kaihami'
import os
#In new Linux ver we need to install libswitch...
#sudo apt-get install libswitch-perl
# use edge-pro -g <genome> - p (<ptt file> -r <rnt file> -u <fastq_file> -v reads2
# -M <insert size (only paired end)> -o <OUTPUT pathway + sample_name>

def Edge_call(Reference_genome, ptt, rnt, R1_file, R2_file, OUTPUT_PATH, M = "500"):
    os.system("/home/kaihami/EDGE_pro_v1.3.1/edge.pl -g " + Reference_genome +
              " -p "+ ptt +
              " -r " + rnt +
              " -u " + R1_file +
              " -v " + R2_file +
              " -M " + M
              + " -o " + OUTPUT_PATH)
    print "Finish"

Main_dir = "/home/kaihami/Desktop/RNA-Seq/"
reference_genome = Main_dir+ "Reference/PAO1_reference.fa"
ptt = Main_dir + "Reference/PAO1_formatted.ptt"
rnt = Main_dir + "Reference/PAO1_formatted.rnt"
output_path = Main_dir + "EDGE-Pro/"

sample1 = "SRR4279875"

sample2 = "SRR4279869"

sample3 = "SRR4279874"

sample4 = "SRR4279873"

sample5 = "SRR4279872"

sample6 = "SRR4279868"
#15675621,
r1_sample1 = "SRR4279875_1"
r2_sample1 = "SRR4279875_2"

r1_sample2 = "SRR4279869_1"
r2_sample2 = "SRR4279869_2"

r1_sample3 = "SRR4279874_1"
r2_sample3 = "SRR4279874_2"

r1_sample4 = "SRR4279873_1"
r2_sample4 = "SRR4279873_2"

r1_sample5 = "SRR4279872_1"
r2_sample5 = "SRR4279872_2"

r1_sample6 = "SRR4279868_1"
r2_sample6 = "SRR4279868_2"

r1_sample_1_path = Main_dir + r1_sample1 + ".fastq"
r2_sample_1_path = Main_dir + r2_sample1 + ".fastq"

r1_sample_2_path = Main_dir + r1_sample2 + ".fastq"
r2_sample_2_path = Main_dir + r2_sample2 + ".fastq"

r1_sample_3_path = Main_dir + r1_sample3 + ".fastq"
r2_sample_3_path = Main_dir + r2_sample3 + ".fastq"

r1_sample_4_path = Main_dir + r1_sample4 + ".fastq"
r2_sample_4_path = Main_dir + r2_sample4 + ".fastq"

r1_sample_5_path = Main_dir + r1_sample5 + ".fastq"
r2_sample_5_path = Main_dir + r2_sample5 + ".fastq"

r1_sample_6_path = Main_dir + r1_sample6 + ".fastq"
r2_sample_6_path = Main_dir + r2_sample6 + ".fastq"

output_path1 = Main_dir + "EDGE-Pro/" + sample1
output_path2 = Main_dir + "EDGE-Pro/" + sample2
output_path3 = Main_dir + "EDGE-Pro/" + sample3
output_path4 = Main_dir + "EDGE-Pro/" + sample4
output_path5 = Main_dir + "EDGE-Pro/" + sample5
output_path6 = Main_dir + "EDGE-Pro/" + sample6

Edge_call(reference_genome, ptt, rnt, r1_sample_1_path, r2_sample_1_path, output_path1, M="500")
print "Finish 1"
Edge_call(reference_genome, ptt, rnt, r1_sample_2_path, r2_sample_2_path, output_path2, M="500")
print "Finish 2"

Edge_call(reference_genome, ptt, rnt, r1_sample_3_path, r2_sample_3_path, output_path3, M="500")
print "Finish 3"
Edge_call(reference_genome, ptt, rnt, r1_sample_4_path, r2_sample_4_path, output_path4, M="500")
print "Finish 4"
Edge_call(reference_genome, ptt, rnt, r1_sample_5_path, r2_sample_5_path, output_path5, M="500")
print "Finish 5"
Edge_call(reference_genome, ptt, rnt, r1_sample_6_path, r2_sample_6_path, output_path6, M="500")
print "Finish 6"
print"""
   /) /)
  ( ^.^ )
 C(") (")
"""
