stari_finale=[]
stari=[]
alfabet=[]
tranzitii=[]
def dfa_minimal(matrice, initial):
    lista=[[-1 for i in alfabet]for j in stari]
    for i in stari:
        for j in alfabet:
            for element in matrice[i]:
                if element!="0":
                    for litera in element:
                        if litera==j:
                            lista[i][alfabet.index(j)]=matrice[i].index(element)



    matrice2 = [[0 for i in stari] for j in stari]
    for i in range(1, len(stari)):
        for j in range(i):
            if i in stari_finale and j in stari_finale or i not in stari_finale and j not in stari_finale:
                matrice2[i][j]=0
            else:
                matrice2[i][j]=1
    ok=1
    while ok!=0:
        ok=0
        for i in range(1, len(stari)):
            for j in range(i):
                if matrice2[i][j]==0:
                    for litera in alfabet:
                        if matrice2[lista[i][alfabet.index(litera)]][lista[j][alfabet.index(litera)]] ==1 or matrice2[lista[j][alfabet.index(litera)]][lista[i][alfabet.index(litera)]]:
                            ok=1
                            matrice2[i][j]=1
    nr=len(stari)
    while ok != 0:
        for i in stari:
            for j in stari:
                print(matrice2[i][j], end=" ")


    stari_nou=[]
    for i in range(1, len(stari)):
        for j in range(i):
            if matrice2[i][j]==0:
                stari_nou.append([i,j])
    for element in stari_nou:
        ok=0
        for stare in element:
            if stare in stari_finale:
                stari_finale.remove(stare)
                ok=1
                stari_finale.append(nr)
            if stare==initial:
                initial=nr
                ok=1
        if ok==1:
            nr+=1
    nr=len(stari)
    for element in stari_finale:
        if stari_finale.count(element)!=1:
            stari_finale.remove(element)



    for element in stari_nou:
        for tranzitie in tranzitii:
            for stare in element:
                if tranzitie[0]==stare:
                    tranzitie[0]=nr
                if tranzitie[2]==stare:
                    tranzitie[2]=nr
        nr+=1

    for i in range (len(stari),nr):
        stari.append(i)
    for element in stari_nou:
        for stare in element:
            if stare in stari:
                stari.remove(stare)
    ok=1
    while ok!=0:
        ok=0
        for element in tranzitii:
            if tranzitii.count(element)!=1:
                ok=1
                tranzitii.remove(element)
    print ("DFA minim:")
    print()
    print("stari finale= ",stari_finale)
    print("starea initiala= ", initial)
    print ("stari= ", stari)
    print("tranzitii: ")
    for tranzitie in tranzitii:
        print("q",tranzitie[0],",",tranzitie[1],",","q",tranzitie[2])
def bonus_dfa_minimal(matrice, initial):
    lista=[[-1 for i in alfabet]for j in stari]
    for i in stari:
        for j in alfabet:
            for element in matrice[i]:
                if element!="0":
                    for litera in element:
                        if litera==j:
                            lista[i][alfabet.index(j)]=matrice[i].index(element)



    matrice2 = [[0 for i in stari] for j in stari]
    for i in range(1, len(stari)):
        for j in range(i):
            if i in stari_finale and j in stari_finale or i not in stari_finale and j not in stari_finale:
                matrice2[i][j]=0
            else:
                matrice2[i][j]=1
    ok=1
    while ok!=0:
        ok=0
        for i in range(1, len(stari)):
            for j in range(i):
                if matrice2[i][j]==0:
                    for litera in alfabet:
                        if matrice2[lista[i][alfabet.index(litera)]][lista[j][alfabet.index(litera)]] ==1 or matrice2[lista[j][alfabet.index(litera)]][lista[i][alfabet.index(litera)]]:
                            ok=1
                            matrice2[i][j]=1
    nr=len(stari)
    while ok != 0:
        for i in stari:
            for j in stari:
                print(matrice2[i][j], end=" ")


    stari_nou=[]
    for i in range(1, len(stari)):
        for j in range(i):
            if matrice2[i][j]==0:
                stari_nou.append([i,j])
    for element in stari_nou:
        ok=0
        for stare in element:
            if stare in stari_finale:
                stari_finale.remove(stare)
                ok=1
                stari_finale.append(nr)
            if stare==initial:
                initial=nr
                ok=1
        if ok==1:
            nr+=1
    nr=len(stari)
    for element in stari_finale:
        if stari_finale.count(element)!=1:
            stari_finale.remove(element)



    for element in stari_nou:
        for tranzitie in tranzitii:
            for stare in element:
                if tranzitie[0]==stare:
                    tranzitie[0]=nr
                if tranzitie[2]==stare:
                    tranzitie[2]=nr
        nr+=1

    for i in range (len(stari),nr):
        stari.append(i)
    for element in stari_nou:
        for stare in element:
            if stare in stari:
                stari.remove(stare)
    ok=1
    scot=[]
    while ok!=0:
        ok=0
        for element in tranzitii:
            if tranzitii.count(element)!=1:
                ok=1
                tranzitii.remove(element)



        for stare in stari:
            okk=0
            ok = 0
            for tranzitie in tranzitii:
                if stare==tranzitie[0] and tranzitie[2]!=stare:
                    ok=1
                    break

            if ok==0:
                okk=1
                stari.remove(stare)
                if stare in stari_finale:
                    stari_finale.remove(stare)
                okk = 1
                while okk != 0:
                    okk=0
                    for tranzitie in tranzitii:
                        if tranzitie[0]==stare or tranzitie[2]==stare:
                            tranzitii.remove(tranzitie)
                            okk=1

    print ("DFA minim:")
    print()
    print("stari finale= ",stari_finale)
    print("starea initiala= ", initial)
    print ("stari= ", stari)
    print("tranzitii: ")
    for tranzitie in tranzitii:
        print("q",tranzitie[0],",",tranzitie[1],",","q",tranzitie[2])











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
                    tranzitii.append(list(lista))

        line=f.readline()
ok=1
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
    for linie in matrice:
        for element in linie:
            if element != "0":
                for litera in element:
                    nr=0
                    for element2 in linie:
                        if ok==0:
                            break
                        if element2!="0":
                            for litera2 in element2:
                                if litera2==litera:
                                    nr+=1
                                    if nr==2:
                                        ok=0
                                        break




    if ok==0:
        print("Dfa invalid")
    else:
        print("Dfa valid")
    # dfa_minimal(matrice,initial)
    # bonus_dfa_minimal(matrice, initial)


















