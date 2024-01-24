# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
# Raspuns :Se foloseste cand avem mai mult de 2 situatii posibile
# Conditiile se evalueaza de sus in jos
# Se executa codul aferent primei conditii adevarate
# Dupa ce s-a gasit cu true, nu se mai verifica ce a mai ramas mai jos
#
# 2. Verifică și afișează dacă x este număr natural sau nu
# Raspuns
# (0,1,2,3...)
x = int(input("x="))
if x <= 0:
    print('Numarul este natural')
else:
    print('Numarul nu este natural')
# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru
# Raspuns:
if x > 0:
    print('Numarul este pozitiv ')
elif x == 0:
    print('Numarul este negativ')
else:
    print('Numarul este negativ')
# 4. Verifică și afișează dacă x este între -2 și 13
# Raspuns:
if -2 <= x <= 13:
    print('este in interval')
else:
    print('Nu este in interval')
# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5
# Raspuns:
y = int(input('Introduceti y'))
diferente = x - y
if diferente < 5: # verifica functia if abs
    print('Diferenta este mai mica decat 5')
else:
    print('Diferenta este mai mica decat 5')
# 6 . Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’
if not (5 <= x <= 27):
    print('Numarul nu se afla in intervalul mentionat')
else:
    print('Numarul  se afla in intervalul mentionat')
    # 7.
    # x și y (int)
    # Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
    if x == y:
        print('x este egal y')
    elif x > y:
        print(f'{x} este mai mare decat {y}')
    else:
        print(f'{y}este mai mare decat {x}')
        if x not in range(5, 27):
            print('Numarul se afla in intervalul mentionat')
        else:
            print('Numarul nu se gaseste in intervalul mentionat')

