#Calculadora Aritmetica 
print ("Calculadora Aritmetica")
print ("Operaciones a realizar +  -  x  *")

operacion = input("seleccione la operacion: ")
x= int(input("ingrese un valor entero #1: "))
y= int(input("ingrese un valor entero #2: "))

if operacion=='+':
    print("La operacion es + : ", x+y)
elif operacion=='-':
    print("La operacion es - : ", x-y)
elif operacion=='*':
    print("La operacion es x : ", x*y)
elif operacion=='/':
    print("La operacion es / : ", x/y)
else:
      print("El operador es diferente a los valores permitidos")