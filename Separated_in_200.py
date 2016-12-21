__author__ = 'kaihami'
""" From a Fasta file separate in 200 sequences"""

def Fasta_div(Input_File, Output_File):
    OpenFile = open(Input_File, "r").read().split("\n")
Input_File = "/home/kaihami/Desktop/RR_files/REC_Final_Fasta/Fasta_teste/FASTA_REConly.txt"
OpenFile = open(Input_File, "r").read().split("\n")
x = 0
w = 0
Output_File = "/home/kaihami/Desktop/RR_files/REC_Final_Fasta/Fasta_teste/FASTA_50_bucket/REC_only/REConly_"
for y in xrange(0, len(OpenFile)):
    head = OpenFile[y]
    if ">" in head:
        x +=1
        if x <= 200:
            with open(Output_File+ "_" + str(w)+ ".txt", "a") as f:
                f.write(OpenFile[y])
                f.write("\n")
                f.write(OpenFile[y+1])
                f.write("\n\n")
        if x == 200:
            x =0
            w+=1
print "finish"
