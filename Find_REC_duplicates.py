__author__ = 'kaihami'
"""
From the Actino_REC.txt, find any protein with more than one REC domain
"""
import os
Dir = "/home/kaihami/Desktop/RR_files/Final_REC/"
save_path = "/home/kaihami/Desktop/RR_files/Final_REC/dup/"
File_lst = []
for File in os.listdir(Dir):
    if File.endswith(".txt"):
        File_lst.append(File)
for path in File_lst:
    Open_File = open(Dir+path, "r").read().split("\n")
    Total = []
    print Dir+path
    for ele in Open_File:
        lsplit = ele.split(",")
        if len(lsplit) > 2:
            Total.append(lsplit)
    name = path.split(",")
    name_final = name[0]
    dup = []
    dup2 = []
    for line in Total:
        locus = line[7]
        if locus in dup:
            dup2.append(locus)
        if locus not in dup:
            dup.append(locus)
    for line in dup2:
        with open(save_path+ name_final+".txt", "a") as f:
            f.write(line)
            f.write("\n")
