from math import sqrt
#el siguiente código realiza operaciones básicas con números complejos (suma, resta, multiplica y cálcula el modulo)

#primero establecemos las funciones que se utilizaran

def pedirNumero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input(""))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
return num

def CrearComplejo(real=0,imaginario=0):
    lista1 = []
    lista1 = [real,imaginario]
return lista1

def SumaComplejo(lista1=[], lista2=[]):
    lista3 = []
    lista3 = [lista1[0]+lista2[0],lista1[1]+lista2[1]]
return lista3

def RestaComplejo(lista1=[], lista2=[]):
    lista3 = []
    lista3 = [lista1[0]-lista2[0],lista1[1]-lista2[1]]
    return lista3

def ProductoComplejos(lista1=[], lista2=[]):
    lista4 = []
    lista4 = [lista1[0]*lista2[0]-lista1[1]*lista2[1],lista1[0]*lista2[1]+lista1[1]*lista2[0]]
return lista4

def ModuloComplejo(lista=[]):
    modulo = 0
    modulo = sqrt(lista[0]**2+lista[1]**2)
return modulo

def ImprimirComplejo(lista=[]):
    if (lista[1]<0):
        return print(lista[0],lista[1],"i")
    else:
        return print(lista[0],"+",lista[1],"i")

salir = False
opcion = 0
while not salir:

	print("deseas ingresar un número complejo, (S/N)")
	exit = input()
	if exit.upper()=="N":
		salir = True

	if exit.upper()=="S":
		print("escriba la parte real")
		real1=float(input())
		print("escriba la parte imaginaria")
		imag1=float(input())

		print("ingresa otro número complejo:")
		real2=float(input("escriba la parte real\n"))
		imag2=float(input("escriba la parte imaginaria\n"))
		c1 = CrearComplejo(real1,imag1)
		c2 = CrearComplejo(real2,imag2)
#        	print("los números ingresados son:")
		print(c1)
		print(c2)
		print("\n\n")

		print("de las siguientes opciones elige una:",end=("\n"))
		print("1.sumar complejos")
		print("2.restar complejos")
		print("3.multiplicar complejos")
		print("4.hallar el modulo de un número complejo")
		print("5.salir")
		opcion = pedirNumeroEntero()

		if opcion == 1:
			ans = SumaComplejo(c1,c2)
			print("la suma es:");ImprimirComplejo(ans)
#			print("la suma es:",ImprimirComplejo(ans)) #si se inserta la suma es de esta forma retorna None
		elif opcion == 2:
			ans = RestaComplejo(c1,c2)
			print("la resta es:")
			ImprimirComplejo(ans)
		elif opcion == 3:
			ans = ProductoComplejos(c1,c2)
			print("la multiplicación es:")
			ImprimirComplejo(ans)
		elif opcion == 4:
			opcion1 = 0
			print("a cual de los dos números le deseas calcular el modulo")
			print("presiona 1, para el primer número ingresado")
			print("presiona 2, para el segundo número ingresado")
			opcion1 = int(input())

			if opcion1 == 1:
				ans = ModuloComplejo(c1)
				print("el modulo es:",ans)
			elif opcion1 == 2:
				ans = ModuloComplejo(c2)
				print("el modulo es:",ans)
			else:
				print("no has elegido una opción correcta")
		elif opcion == 5:
			salir = True
		else:
			print("nos ha elegido una opción correcta")
print("intentalo mas tarde")
