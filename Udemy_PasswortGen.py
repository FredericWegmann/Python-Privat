import random
'''student_heights = input().split()
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])
count = 0 
for n in student_heights:
    count += n
print(f"Total Height: {count}")

number = 0
for student in student_heights:
    number += 1
print(f"Number of students: {number}")

average = round(count/number, 2)
print(f"The average height is: {average}")'''

#highest score 
'''student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

num = len(student_scores)
highest = 0
for i in student_scores:
    if i > highest:
        highest = i
print(highest)'''

#adding up numbers from range, but only even numbers
'''last_number = int(input("Type in a number between 1 and 1000 to sum up all even numbers! \n"))

sum = 0 
for i in range(1, last_number + 1):
    if i % 2 == 0:
        sum += i
print(f"The sum of all even numbers between 1 and {last_number} is {sum}!") '''

#FizzBuzz:
'''for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)'''

#Passwort Generator:
'''buchstaben = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
nummern = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbole = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

nmr_buchstaben = int(input("Wie viele Buchtaben?\n"))
nmr_nummern = int(input("Wie viele Zahlen?\n"))
nmr_symbole = int(input("Wie viele Symbole?\n"))
passwort_len = nmr_buchstaben + nmr_nummern +  nmr_symbole
passwort = ""
pool = []
for n in range(0, nmr_buchstaben):
    rand_buchstabe = random.randint(0, len(buchstaben) - 1)
    pool.append(buchstaben[rand_buchstabe])

for m in range(0, nmr_nummern):
    rand_nummer = random.randint(0, len(nummern) - 1)
    pool.append(nummern[rand_nummer])

for p in range(0, nmr_symbole):
    rand_symbol = random.randint(0, len(symbole) - 1)
    pool.append(symbole[rand_symbol])

random.shuffle(pool)

for i in range(0, passwort_len):
    passwort += pool[i]
print(passwort)'''



'''for n in range(0, nmr_buchstaben):
    rnd_nummer = random.randint(0, len(buchstaben) - 1)
    passwort += buchstaben[rnd_nummer]
for n in range(0, nmr_nummern):
    rnd_nummer = random.randint(0, len(nummern) - 1)
    passwort += nummern[rnd_nummer]
for n in range(0, nmr_symbole):
    rnd_nummer = random.randint(0, len(symbole) - 1)
    passwort += symbole[rnd_nummer]'''
for i in range(1, 6):
    print(i)