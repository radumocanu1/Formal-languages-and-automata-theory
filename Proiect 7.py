#Mocanu Radu, Muscalu Diana, Micu Roberta
# am modificat putin codul de la ex2 adaugand un "SPACE" la inceputul tape-ului (pt a identifica primul element al acesteia)
# pozitia initiala de pe care porneste head-ul se modifica, fiind 1 (primul simbol de dupa "SPACE")
# se citesc cele doua input-uri (tape-uri) si se concateneaza astfel tape1 + tape2, cele doua TM fiind echivalente
# functia delta verifica daca prima jumatate a tape-ului (adica fostul prim tape) este egala cu cea de-a doua jumatate (adica fostul tape2)

import copy

delta = {} #dictionar ce are ca cheie un tuplu format din doua elemnte: starea si simbolul acesteia
states = set() #multimea starilor
sigma = set() #alfabetul
tapesymbols = [] #simbolurile de pe tape
S = "" #stare initiala
A = "" #stare de acceptare
R = "" #stare de respingere

#functie pentru validare de masina turing
def check_TM():
    global S
    global A
    global R
    global delta
    with open('date4.in', 'r') as f: #citim inputul din fisier
        line = f.readline()
        while line != '':
            if line[0] != "#": #verificam daca pe linia curenta e de fapt un comentariu
                if line[0] == "S" and line[1] == "t": #aici verificam daca citim stari
                    while True:
                        line = f.readline()
                        if line[0] == "E": #daca dam de End am citit toate starile si ne oprim
                            break
                        ls = line.split(",")
                        ls[0] = ls[0].strip()
                        states.add(ls[0])
                        if len(ls) > 1:
                            if ls[1] == ' s\n':
                                S += ls[0]
                            if ls[1] == ' a\n':
                                A += ls[0]
                            if ls[1] == ' r\n':
                                R += ls[0]

                if line[0] == "D": #aici verificam daca citim functia
                    while True:
                        line = f.readline()
                        if line[0] == "E":
                            break
                        i = 0
                        part1 = ""
                        part2 = ""
                        ok = 0
                        for i in range(0, len(line)-1):
                            if line[i] == "-":
                                ok = 1
                            if ok == 0 and line[i] != " ":
                                part1 += line[i]
                            if ok == 1 and line[i] != " ":
                                part2 += line[i]

                        t = tuple(part1.split(",")) #aici formam tuplul pentru cheia dictionarului
                        part2 = part2[2:].split(",")
                        lss = list(part2)
                        delta[t] = lss #pentru fiecare cheie avem o lista ce retine starea urmatoare si simbolul ei, cat si directia de deplasare

                if line[0] == "S" and line[1] == "i": #aici verificam daca citim sigma(alfabetul)
                    while True:
                        line = f.readline()
                        if line[0] == "E":
                            break
                        s = line.strip()
                        sigma.add(s)

                if line[0] == "T": #aici verificam daca citim simbolurile de pe tape
                    while True:
                        line = f.readline()
                        if line[0] == "E":
                            break
                        s = line.strip()
                        tapesymbols.append(s)
            line = f.readline()

    ok = 1 #presupunem ca este o masina turing valida
    for x in delta.keys(): #verificam intai in cheile din dictionar daca starile si simbolurile sunt valide
        if x[0] not in states and x[0] != '#':
            ok = 0
        if x[1] not in tapesymbols and x[1] != '#':
            ok = 0

    for x in delta.values(): #verificam dupa aceea printre valorile din dictionar daca starile si simbolurile sunt valide
        if x[0] not in states and x[0] != '#':
            ok = 0
        if x[1] not in tapesymbols and x[1] != '#':
            ok = 0

    if ok == 1: #iar la final verificam daca sigma se regaseste preintre simbolurile tape-ului
        for e in sigma:
            if e not in tapesymbols:
                ok = 0

    return ok



#function grammar() loads the cfg_config_file
#print(states)
#print(S, A, R)
#print(delta)
#print(sigma)
#print(tape)

def simulator(tape):

        # global tape
        # tape = list(input)

        pos = 1 #positia initiala
        stare_curenta = S #starea initiala

        while stare_curenta not in [A, R]: #cat timp n-am ajuns intr-o stare finala(acceptare sau respingere)
            #pentru a vedea modul de parcurgere al tape-ului decomentati
            #print(tape)
            if pos >= len(tape): #in cazul in care trebuie sa mergem la dreapta si ne aflam pe ultima pozitie adaugam un spatiu
                tape.append("SPACE")

            key = (stare_curenta, str(tape[pos])) #ne deplasam in starea urmatoare


            if key not in delta.keys():                 #verifica daca ceva e in neregula cu input-ul
                print("EROARE, NU AJUNGE IN STARILE FINALE")
                return

            tape[pos] = delta[key][1] #modificam valoarea curenta de pe tape
            stare_curenta = delta[key][0] #ne luam urmatoarea stare

            if delta[key][2] == "R": #ne deplasam la dreapta
                if pos >= len(tape):
                    tape.append("SPACE")
                pos += 1

            if delta[key][2] == "L": #ne deplasam la stanga
                if pos > 0:
                    pos -= 1

        if stare_curenta == A: #verificam daca e acceptat sau nu
            return 1
        else:
            return 0


def verify_simulator(tape2):
        pos = 1 #positia initiala
        stare_curenta = S #starea initiala

        while stare_curenta not in [A, R]: #cat timp n-am ajuns intr-o stare finala(acceptare sau respingere)
            #pentru a vedea modul de parcurgere al tape-ului decomentati
            #print(tape)
            if pos >= len(tape2): #in cazul in care trebuie sa mergem la dreapta si ne aflam pe ultima pozitie adaugam un spatiu
                tape2.append("SPACE")

            key = (stare_curenta, str(tape2[pos])) #ne deplasam in starea urmatoare


            if key not in delta.keys():                 #verifica daca ceva e in neregula cu input-ul
                print("EROARE, NU AJUNGE IN STARILE FINALE")
                return

            tape2[pos] = delta[key][1] #modificam valoarea curenta de pe tape
            stare_curenta = delta[key][0] #ne luam urmatoarea stare

            if delta[key][2] == "R": #ne deplasam la dreapta
                if pos >= len(tape2):
                    tape2.append("SPACE")
                pos += 1

            if delta[key][2] == "L": #ne deplasam la stanga
                if pos > 0:
                    pos -= 1

        if stare_curenta == A: #verificam daca e acceptat sau nu
            return 1
        else:
            return 0

if check_TM() != 1: #verificam intai daca este o masina turing valida
    print("TM INVALID")
else:
    print("TM VALID")
    input = input("Dati inputul: ")
    tape = []
    tape.append("SPACE")
    tape.extend(list(input))  #formam o banda cu inputul citit(tape-ul)


    tape2 = copy.deepcopy(tape) #facem o copie a benzii


    sim1 = simulator(tape)


    sim2 = verify_simulator(tape2)


    if sim1 != sim2: #verificam acceptarea cuvantului folosind copia de backup
        print("EROARE LA STOCAREA BENZILOR")
    elif sim2 == 1:
        print("ACCEPTED")
    else:
        print("NOT ACCEPTED")