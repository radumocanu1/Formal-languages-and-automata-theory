stari_finale=[]
stari=[]
alfabet=[]
tranzitii=[]
initial=-1
ok=1
with open('fisier.in1', 'r') as f:
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
    print("DFA invalid")
else:

    matrice=[[str(0) for i in stari] for j in stari]
    for tranzitie in tranzitii:
        if matrice[tranzitie[0]][tranzitie[2]]!="0":
            c=matrice[tranzitie[0]][tranzitie[2]]
            matrice[tranzitie[0]][tranzitie[2]]=c+tranzitie[1]
        else:
            matrice[tranzitie[0]][tranzitie[2]]=tranzitie[1]
    for i in stari:
        for j in stari:
            print(matrice[i][j], end=" ")
        print()
    for linie in matrice:
        for element in linie:
            if element!="0" and linie.count(element)>1:
                ok=0

    if ok==0:
        print("Dfa invalid")
    else:
        print("Dfa valid")
        cuvant=input("cuvant=")
        litera_curenta=cuvant[0]
        ok=0
        for element in matrice[initial]:
            if element.isdigit()==False:
                for litera in element:
                    if litera==litera_curenta:
                        ok=1
                        linie=matrice[initial].index(element)
            if ok==1:
                break

        if ok==0:
            print("cuvant invalid")
        else:
            i=1
            while ok==1 and i<=len(cuvant)-1:
                ok=0
                litera_curenta=cuvant[i]
                for element in matrice[linie]:
                    if element.isdigit() == False:
                        for litera in element:
                            if litera == litera_curenta:
                                ok = 1
                                linie = matrice[linie].index(element)

                    if ok==1:
                        break
                i=i+1
        if linie in stari_finale:
            print("cuvant valid")
        else:
            print("cuvant invalid")