#Pilas 

from collections import deque
from traceback import print_last

#declaración de PILA 
Pila = deque()
i=0

while True:
    i+=1
    #apilar elementos 
    Pila.append("elmento {}".format(i))
    print("\n Se agregó un elemento a la Pila")
    print("\n", Pila)

    if input("desea apilar otro elemento [s/n]: ") =="n":
        break

print("{}".format(Pila))

while len(Pila) >0:
    elemento = Pila.pop()
    print("\n Se des aplilo un elmeento a la Pila {}".format(elemento))

    #mostrar pila 
    print(Pila)
    