__author__ = 'kaihami'
#TODO alguma coisa errada...
import os

trained = open("/home/kaihami/Desktop/Python/Captcha_images/Test_data/Test_trained.txt", "r").read().split("\n")
non_trained = open("/home/kaihami/Desktop/Python/Captcha_images/Test_data/Test_original.txt", 'r').read().split("\n")

trained_ls = []

for line in trained:
    if len(line.split("\t"))>1:
        trained_ls.append(line.split("\t"))

non_trained_ls = []
for s in non_trained:
    print s
    if len(s.split("\t")) >1:
        non_trained_ls.append(s.split("\t"))

expected = open("/home/kaihami/Desktop/Python/Captcha_images/Test_data/Expected_results.txt","r").read().split("\n")

expected_ls = []
for n in expected:
    if len(n.split("\t"))>1:
        expected_ls.append(n.split("\t"))

#create a dict
results_dict = {}

for ele in expected_ls:
    name, result = ele[0], ele[1]
    results_dict[name] = result

final_results = {}
for k, v in results_dict.items():
    for ele in non_trained_ls:
        for a in trained_ls:
            name_t, result_train = a[0], a[1]
            name_n, result_non = ele[0],ele[1]
            result_real = v
            if name_t == k and name_n == k:
                final_results[k] = [result_real, result_non, result_train]
for ke, va in final_results.items():
    na = ke
    real, test, train = va[0], va[1], va[2]
    real_test = 0
    if real == test:
        real_test = 1
    real_train = 0
    if real == train:
        real_train = 1
    ls = [na, real, test, train, str(real_test), str(real_train)]
    with open("/home/kaihami/Desktop/Python/Captcha_images/Test_data/Final_results.txt", "a") as f:
        f.write("\t".join(ls))
        f.write("\n")
print "Finish"