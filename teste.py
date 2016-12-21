import random

#1	2	11	13	24
x = 0
ori = [1,2,11,13,24]
f = []
while x <18:
    lst = [3,4,5,6,7,8,9,10,12,14,15,16,17,18,19,20,21,22,23,25]
    a = random.sample(lst, 11) + ori
    b = sorted(a)
    if b not in f:
        f.append(b)
        x+=1
print "ok"
f_s = []
for s in f:
    f_s.append([str(x) for x in s])
for game in f_s:
    with open("jogo.txt", "a") as fi:
        fi.write("\t".join(game))
        fi.write("\n")