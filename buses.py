import time
import os
from random import randint

def buses (n1,n2):
    print(115*"-")
    print( (n1*" ") + "_______________"         + ((100-n1)*" " )+"|" )
    print( (n1*" ") + "|__|__|__|__|__|___"     +((97-n1)*" " )+"|" )
    print( (n1*" ") + "|   BUSNUMERO1     |"    +((96-n1)*" " )+"|" )
    print( (n1*" ") + "|----0----------0--|"    +((96-n1)*" " )+"|" )
    print(115*"-")
    print( (n2*" ") + "_______________"         + ((100-n2)*" " )+"|" )
    print( (n2*" ") + "|__|__|__|__|__|___"     +((97-n2)*" " )+" |" )
    print( (n2*" ") + "|  BUSNUMERO2X     |"    +((96-n2)*" " )+" |" )
    print( (n2*" ") + "|----0----------0--|"    +((96-n2)*" " )+" |" )
    print(115*"-")
    return 'Carrera de Buses'

a = 0
b = 0

print("CARRERA DE BUSES!!!")
print("BUSNUMERO1   VS   BUSNUMERO2X")
time.sleep(3)
os.system("cls")

while (a < 97) and (b < 97):
    c = randint(1,2)
    if c == 1:
        a += 1
    if c == 2:
        b += 1
    os.system("cls")
    print(buses(a,b))
    time.sleep(0.05)

if a == 97:
    gano = "BUSNUMERO1"
if b == 97:
    gano = "BUSNUMERO2X"

print("GANO "+gano+"!!!")
