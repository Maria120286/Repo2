sirr='Salut  lume'
#feliem stringul,ne folosim de indexare
sir1=sirr[0:5]
print(sir1)
sir2=sirr[7:]
print(sir2)
sir3 = sirr[:5]
print(sir3)
sir = sirr [2:    9      :2]
         # start , stop, step
print(sir)
sirr4=sirr [: : 2]
print(sirr4)
# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
# if si else permite controlul fluxului unui program permitand executia unor blocuri specifice de cod in funcrtie de valoare
# daca conditia if este adevarata se executa blocul de cod care urmeza dupa if

# 2 verifica si afiseaza daca x este numar natural sau nu
# (0,1,2,3.....)
x=int(input('x este egal cu :'))
if x >= 0:
    print('Numarul este natural')
else:
    print('Numarul nu este natural')
# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
if x > 0:
    print('Numarul este pozitiv')
elif x==0:
    print('Numarul este neutru')
else:
    print('Numarul este negativ')
# 4. Verifică și afișează dacă x este între -2 și 13.
if -2<= x <= 13:
    print('Numarul este in interval')
else:
    print('Numarul nu se afla in interval')
# 5 Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
y=int(input('Introduceti y'))
diferente = x-y
if diferente <5:
    print('Diferenta este mai mica decat 5')
else:
    print('Diferenta este mai mica decat 5')
# 6 . Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’
if not (5<= x <= 27):
    print('Numarul nu se afla in intervalul mentionat')
else:
    print('Numarul  se afla in intervalul mentionat')
# 7.
# x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
if x==y:
    print('x este egal y')
elif x>y:
    print(f'{x} este mai mare decat {y}')
else:
    print(f'{y}este mai mare decat {x}')
    if x not  in range (5,27 ):
        print('Numarul se afla in intervalul mentionat')
    else:
        print('Numarul nu se gaseste in intervalul mentionat')




