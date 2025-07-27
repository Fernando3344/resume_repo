# determinar el mayor de tres numeros dados.

num1 = int(input("ingrese el primer numero entero: "))
num2 = int(input("ingrese el segundo numero entero: "))
num3 = int(input("ingrese el tercero numero entero: "))

if num1 != num2 and num1 != num3 and num2 != num3:
    if num1 > num2 and num1 > num3 :
    #print("El numero 1 es el mayor de los tres")
      print("de {},{},{} el mayor es {}".format(num1,num2,num3,num1))
    elif num2 > num1 and num2 > num3 : 
     print("El numero 2 es el mayor de los tres")
    else :
     print("El numero 3 es el mayor de los tres")
else :
    print("los numeros debe de ser distintos")