import random

#random_integer = random.randint(1, 20)
#print(random_integer)
#random_float = random.random()
#print(random_float * random_integer)

#Kopf oder Zahl:
#random_num = random.randint(1, 2)
#if random_num == 1 :
#    print("Kopf\n")
#else:
#    print("Zahl\n")

#Lists:
#states_of_america = ["Delaware", "Pennsylvania"]
#print(states_of_america[1])

#states_of_america.append("Washington")
#states_of_america.extend(["Angelalend", "popo"])
#print(states_of_america)

#Lists exercise:
#personen = ["Anton", "Flo", "Freddi", "Alex", "Lucas", "Vroni", "Leopold"]
#anzahl = len(personen)
#zahl = random.randint(0, anzahl - 1)
#print(f"{personen[zahl]} muss heute zahlen!")

#Liste in Liste
#fruits = ["Erdbeere", "Apfel"]
#gemüse = ["Kartoffel", "Bohne"]
#alles = [fruits, gemüse]
#print(alles[1][1])

#Map und treasure
"""
line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map = [line1, line2, line3]

position = input("Wo willst du den Schatz verstecken?")
position_liste = list(position)

if position_liste[0] == "A":
    position_liste[0] = 0
elif position_liste[0] == "B":
    position_liste[0] = 1
elif position_liste[0] == "C":
    position_liste[0] = 2

position_liste[1] = int(position_liste[1]) - 1   

map[position_liste[1]][position_liste[0]] = "X"
print(f"{line1}\n{line2}\n{line3}")
"""

# Schere, Stein, Papier:
schere = """
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
"""
papier = """
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|   
"""
stein = """
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
                     
"""

liste = [schere, stein, papier]
zeichen = int(input("Was nimmst du? 0 für Schere, 1 für Stein und 2 für Papier.\n"))
gegner = liste
random_zahl = random.randint(0, 2)
print(f"Du wählst:\n{liste[zeichen]}\n")
print(f"Computer nimmt:\n{gegner[random_zahl]}\n")
if gegner[random_zahl] == liste[zeichen]:
    print("Unentschieden! Spiele nochmal!")
elif gegner[random_zahl] == schere and liste[zeichen] == papier:
    print("Du verlierst!")
elif gegner[random_zahl] == stein and liste[zeichen] == papier:
    print("Du gewinnst!")
elif gegner[random_zahl] == schere and liste[zeichen] == stein:
    print("Du gewinnst!")
elif gegner[random_zahl] == stein and liste[zeichen] == schere:
    print("Du verlierst!")
elif gegner[random_zahl] == papier and liste[zeichen] == schere:
    print("Du gewinnst!")
elif gegner[random_zahl] == papier and liste[zeichen] == stein:
    print("Du verlierst!")
