#Askisi 13

import math
file_to_open = input("Dwste arxeio:")
try:
    file = open(file_to_open, "r")
except FileNotFoundError:
    print("To arxeio den vrethike.Prospathiste ksana.")
    exit(1)


lst = []
count = -1
strng = file.read()
for x in range(len(strng)):
        count += 1
        lst.append(strng[x])          #Vazoume stin lst ola ta stoixeia toy keimenou strng

file.close()
list2 = []
for x in range(len(lst)):
    list2.append(lst.count(lst[x]))

listPerCent = []
x = "0"
for j in lst:
    x = list2[j] / count * 100

    listPerCent.append(x)
for p in list2:
    print(lst[p], ":", listPerCent[p], "%")