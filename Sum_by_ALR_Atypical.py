__author__ = 'kaihami'
"""
Sum by ALR, Atypical, D1, Typical,
and function (e.g.DNA-binding).
"""

Open = open("/home/kaihami/Desktop/RR_files/MAFFT_1_lista/Total_RR_MAFFT_1.txt", "r").read().split("\n")

Head = "bac_name,CDS,Reconly_Typical,Reconly_D1,Reconly_Atypical,Reconly_ALR,\
OmpR_Typical,OmpR_D1,OmpR_Atypical,OmpR_ALR,NarL_Typical,NarL_D1,\
NarL_Atypical,NarL_ALR,NtrC_Typical,NtrC_D1,NtrC_Atypical,NtrC_ALR,\
LytR_Typical,LytR_D1,LytR_Atypical,LytR_ALR,ActR_Typical,ActR_D1,\
ActR_Atypical,ActR_ALR,YesN_Typical,YesN_D1,YesN_Atypical,YesN_ALR,\
AmiR_Typical,AmiR_D1,AmiR_Atypical,AmiR_ALR,WspR_Typical,WspR_D1,\
WspR_Atypical,WspR_ALR,PleD_Typical,PleD_D1,PleD_Atypical,PleD_ALR,\
FimX_Typical,FimX_D1,FimX_Atypical,FimX_ALR,PvrR_Typical,PvrR_D1,\
PvrR_Atypical,PvrR_ALR,RpfG_Typical,RpfG_D1,RpfG_Atypical,RpfG_ALR,\
HybridHisK_Typical,HybridHisK_D1,HybridHisK_Atypical,HybridHisK_ALR,\
RssB_Typical,RssB_D1,RssB_Atypical,\
RssB_ALR,CheB_Typical,CheB_D1,CheB_Atypical,CheB_ALR,CheV_Typical,CheV_D1,\
CheV_Atypical,CheV_ALR,Others_Typical,Others_D1,Others_Atypical,Others_ALR"

del Open[0]
a = 0
for line in Open:
    lsplit = line.split(",")
    if len(lsplit) > 2:
        for x in xrange(2, (len(lsplit)-1),4):
            #x = 2 ::Only
            a += int(lsplit[x]) #Typical!!!!

