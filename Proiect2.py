
# AM NOTAT EPSILON CU VALOAREA "E", IN APENDIX


def validare(matrice, linie_curenta, cuvant, index):

   for i in range(len(stari)):
       for litera in matrice[linie_curenta][i]:
           if litera == "e":
               validare(matrice, i, cuvant, index)
   global verif
   if index==len(cuvant):
       if linie_curenta in stari_finale:
           verif=1
           return 1
   else:

       for i in range(len(stari)):
           if matrice[linie_curenta][i].isdigit() == False:
               for litera in matrice[linie_curenta][i]:
                   if litera == cuvant[index]:
                       validare(matrice, i, cuvant, index+1)









stari_finale=[]
stari=[]
alfabet=[]
tranzitii=[]
initial=-1
ok=1
with open('fis.in', 'r') as f:
    line=f.readline()
    while line!='':
        if line[0]!="#":
            if line[0]=="S" and line[1]=="t":
                while line[0]!="E":
                    line=f.readline()
                    for caracter in line:
                        if caracter.isdigit()==True:
                            stari.append(int(caracter))
                        if caracter == "S":
                            if initial!=-1:
                                ok=0
                            else:
                                initial = stari[-1]
                        elif caracter == "F":
                            stari_finale.append(stari[-1])
            if line[0]=="S" and line[1]=="i":
                line=f.readline()
                while line[0]!="E":
                    for caracter in line:
                        if caracter.isalpha()==True:
                            alfabet.append(caracter)
                    line = f.readline()
            if line[0]=="T":
                line = f.readline()
                while line[0]!="E":
                    lista=[]
                    for i in range (0,len(line)):
                        if line[i].isdigit()==True:
                            lista.append(int(line[i]))
                        if line[i-1]=="," and line[i+1]==",":
                            lista.append(line[i])
                    line=f.readline()
                    tranzitii.append(tuple(lista))

        line=f.readline()
for element in tranzitii:
    if element[0] not in stari or element[2] not in stari:
        ok=0
        break
    if element[1] not in alfabet:
        ok=0
        break
if ok==0:
    print("NFA invalid")
else:
    print("NFA valid")
    matrice = [[str(0) for i in stari] for j in stari]
    for tranzitie in tranzitii:
        if matrice[tranzitie[0]][tranzitie[2]] != "0":
            c = matrice[tranzitie[0]][tranzitie[2]]
            matrice[tranzitie[0]][tranzitie[2]] = c + tranzitie[1]
        else:
            matrice[tranzitie[0]][tranzitie[2]] = tranzitie[1]
    for i in stari:
        for j in stari:
            print(matrice[i][j], end=" ")
        print()
    linie_curenta=initial
    verif=0
    cuvant=input("Scrieti cuvantul aici: ")
    validare(matrice, linie_curenta, cuvant, 0)
    if verif==1:
        print("Cuvant acceptat")
    else:
        print("Cuvantul nu a fost validat")