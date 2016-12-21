__author__ = 'kaihami'
"""
Vou usar para ver quais proteinas tem o dominio verdadeiramente REC.

Find all REC domains in the Final_REC file => this file contains all information + REC domain information
output a file containg the locus_tag without dup
I'll use the output to find which genes really contains REC domain back to RR_Fasta_xx_formatted
"""

import os

fi1 = "/home/kaihami/Desktop/RR_files/Final_REC/dup/old/Alpha_REC.txt"

fi1_open = open(fi1, "r").read().split("\n")

total = []

for line in fi1_open:
    lsplit = line.split(",")
    if len(lsplit) >2:
        total.append(lsplit)
remove_dup = []
for ele in total:
    locus = ele[7]
    if locus not in remove_dup:
        remove_dup.append(locus)