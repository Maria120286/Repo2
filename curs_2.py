# Operatori

# Operatorii de atribuire
x = 10
print(x)

# Operatori cu adumnare
y = 5
y = 5 + 3  # se poate asa
y += 3
print(y)

# operatori de scadere
z = 10
z = 4
print(z)

# operatori de inmultire
a = 2
a *= 5
print(a)

# operatori de impartire
b = 10
b /= 5
print(b)

# operator cu ridicare la putere
c = 3
c **= 4
print(c)

# operatori aritmetici
salariu = 4325
suma_adunare = salariu + 50
print(suma_adunare)

suma_scadere = (salariu - 50)
print(suma_scadere)

inmultire = salariu * 50
print(inmultire)

modulo = 11 % 2
print(modulo)
exponential = 2 ** 3
print(exponential)

floor_division = 18 // 3
print(floor_division)
# operator de comparare

a = 5
b = 10

# operator de egalitae
is_equal = (a == b)
print(is_equal)

# operatori in not egal
is_notegal = (a != b)
print(is_notegal)

# operator greater than equal
is_greaterequal = (b >= c)
print(is_greaterequal)

# operator less than
less_than = (a > c)
print(less_than)

# operator greater thet
greator_than = (b > c)
print(greator_than)

# operator logici (and,not,or)
a = 10
b = 5
c = 7
print('...............................')
# utiliozare operatorului and itr-o expresie
rezultat_and = (a > b) and (a > c)
print(rezultat_and)  # utilizarea operatorului 'or '  intr-o
rezultat_or = (a > b) or (a > c)
print(rezultat_or)
# utiliozare operatorului 'not'o expresie
rezultat_not = not (b < a)
print(rezultat_not)
# IF, IF ELSE ,     Flow control
nota_de_trecere = 4.15
nota: float = float(input('alege nota'))
if nota >= nota_de_trecere:
    print(f'Ai luat nota {nota}')
print(f'Felicitari ai trecut examenul')
# else

print('Ai picat examenul')
print(30 * '-')

angajat = True

if angajat:
    print('Angajatul este prezent la serviciu')
print('Continua activitatile de lucru')

# else
print('Angajatul este absent la serviciu ')
print('Se iau masuri pentru absente')
# elif
varsta = 18
# if_varsta < 18
print('Nu este inca major')


print(' Ai exact 18 ani .Felicitari pentru majorat')
import datetime

an_nastere = int
input('Introduceti anul nasterii ')
an_actual = datetime.date.today().year
varsta = an_actual - an_nastere
print('Acces permis')
#else
print('Acces restrictionat.Trebuie sa ia 18 ani')

# String Slicing-
sirr = 'Salut lume'
sirr1 = sirr[0:5]

