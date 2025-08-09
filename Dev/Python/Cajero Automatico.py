#Cajero Automatico 
from random import randrange

saldo = randrange(0,500)
print ("Bienvenido al Cajero automatico")
print()
print("Opciones Disponibles:")
print("1. Consulta de Saldo disponible")
print("2. Extraer Dinero")
print("3. Depositar Dinero")
print("4. Transferencias")
print("5. Salir")

Operacion = int(input("Seleccione la Opción del Cajero: "))

if Operacion in range(6):
    if Operacion == 5:
        print ("hasta luego")
    elif Operacion == 1:
        print ("su saldo disponible es: ", saldo)
    elif Operacion == 2:
        monto = int(input("indique Monto a retirar: "))
        if monto>saldo:
          print ("Saldo No Disponible", monto)
        else:
            saldo=saldo-monto
            print ("Retire su dinero del depensador",monto)
            print ("Saldo Actual es:",saldo)
    elif Operacion == 3:
            monto = int(input("indique Monto a depositar: "))
            saldo=saldo-monto
            print ("deposite su dinero del depensador",monto)
            print ("Saldo Actual es:",saldo)
    elif Operacion == 4:
            cuenta = input("Ingrese el nuemero de cuenta a transferir: ")
            monto = int(input("indique Monto a trasnferir: "))
            if monto>saldo:
                print ("No se puede realizar la transferencia, saldo insuficiente")
            else:
                #saldo=saldo-monto
                saldo = saldo - monto
                print ("Transferencia realizada con exito: ",cuenta, " Saldo actual: ",saldo)
                