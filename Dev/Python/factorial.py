
#Factorial de un número con función recursiva. 

def Factorial(N):
    if N == 0:
        return 1
    else:
        return (N * Factorial(N-1))
    
def Principal():
    Num = int(input("Introduzca número entero positivo:"))
    if Num <0:
        print("El número debe ser positivo")
    else: 
        print("El Factorial del número {} es: {}".format(Num,Factorial(Num)))

Principal()