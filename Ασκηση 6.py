#Askisi 6


lst = [0, 0, 0]


def thresh(i, j):
    list2 = []
    for x in range(len(i)):
        for y in range(len(i)):
            for z in range(len(i)):                                    #Sunartisi evresis pithanwn sundiasmwn
                if i[x] != i[y] and i[y] != i[z] and i[x] != i[z]:
                    if i[x]+i[y]+i[z] > str(j):
                        list2.append(i[x]+i[y]+i[z])

    print(list2)


print("Doste 3 arithmous :")
lst[0] = input()
lst[1] = input()                    #egrapsa me grekklish giati den etrexe me ellinika
lst[2] = input()

mySet = set(lst)


t = 200
if len(lst) != len(mySet):
    print("Kapoios arithmos epanalamvanetai")
else:
    thresh(lst, t)
