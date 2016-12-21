import re
path = "/home/kaihami/Desktop/Genes_overXempty_SigX_Hausler"
text = open(path, 'r').read().split('\n')
new_list = []
for line in text:
        if "PA14_" in line:
                a = line.split(' ')
                new_list.append(a[0])

for element in new_list:
        to_write = open('/home/kaihami/Desktop/teste2.txt', 'a')
        le = element.replace("'","")
        to_write.write(le + "\n")
        to_write.close()

PATH2 = "/home/kaihami/Desktop/teste.txt"
minha_lista = open(PATH2, 'r').read().split('\n')


nova_lista = []
nova_lista2 = []
for line in minha_lista:
        a = line.split('\t')
        for x in a:
                if "PA14_" in x:
                        nova_lista.append(x.replace('"', ""))

compare = open('/home/kaihami/Desktop/teste2.txt', 'r').read().split('\n')

for element in nova_lista:
        if element in compare:
                nova_lista2.append("yes")
        else:
                nova_lista2.append("no")

import random

number = random.randrange(1, 100)
print(number)

guess = False

while not guess:
    usr_ipt = int(input("Guess a number: "))
    if usr_ipt == number:
        print("You guessed it!"

    if usr_ipt > number:
        print("Too high")
    if usr_ipt < number:
        print("Too low")