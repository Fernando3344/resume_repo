#colas

from collections import deque

#declaracion cola
cola = deque()

i=0
while True: 
    i+=1
    cola.append("elemento {}".format(i))
    print("\n se agrego elemento a la cola")
    print("\n")
    print(cola)

    if input("desea ingresar otro elemento [s/n]: ") == "n":
        break

print(cola)

#desencolar los elementos

while len(cola)>0:
    elemento  = cola.popleft()
    print("El elmento a desencolar {}".format(elemento))

print(cola)