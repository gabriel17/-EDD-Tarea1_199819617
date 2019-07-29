import os
import time
from ListaSimple import ListaSimple

lst = ListaSimple()

if os.name == "posix":
   var = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

def AgregarInicio():
	os.system(var) 
	opSbMenu = 0
	print ("""
*****************************************************************
***************  Agregando al inicio en la lista  ***************
*****************************************************************
""")
	pDato = input("Escriba el Dato a Ingresar: ")
	lst.insertar_inicio(pDato)

	while opSbMenu != 99:
		resp = str (input("Desea Agregar Otro Dato: s/n? "))
		if resp == "s":
			opSbMenu = 0
			pDato = input("Escriba el Dato a Ingresar: ")
			lst.insertar_inicio(pDato)
		elif resp == "S":
			opSbMenu = 0
			pDato = input("Escriba el Dato a Ingresar: ")
			lst.insertar_inicio(pDato)
		else:
			opSbMenu = 99

def AgregarFin():
	os.system(var) 
	opSbMenu = 0
	print ("""
*****************************************************************
***************  Agregando al final  en la lista  ***************
*****************************************************************
""")
	pDato = input("Escriba el Dato a Ingresar: ")
	lst.insertar_fin(pDato)

	while opSbMenu != 99:
		resp = str (input("Desea Agregar Otro Dato: s/n? "))
		if resp == "s":
			opSbMenu = 0
			pDato = input("Escriba el Dato a Ingresar: ")
			lst.insertar_fin(pDato)
		elif resp == "S":
			opSbMenu = 0
			pDato = input("Escriba el Dato a Ingresar: ")
			lst.insertar_fin(pDato)
		else:
			opSbMenu = 99

def Recorrer():
	os.system(var) 
	print ("""
*****************************************************************
***************       Recorrido de la lista       ***************
*****************************************************************
""")
	opSbMenu = 0
	if lst.listavacia() == True:
		print("La lista esta vacia \n")
		input("Presione una tecla para continuar")
	else:	
		lst.listar()	
		input("Presione una tecla para continuar \n")

def ModificarDato():
	os.system(var) 
	print ("""
*****************************************************************
***************  Modificar un datos de la lista   ***************
*****************************************************************
""")
	lDato =""
	bDato = ""
	if lst.listavacia() == True:
		print("La lista esta vacia \n")
		input("Presione una tecla para continuar: ")
	else:
		lst.listar()
		opSbMenu = 0
		lDato = str(input("Ingrese el dato a Modificar: "))
		bDato = str(input("Ingrese el nuevo Dato: "))
		lst.modificar(lDato,bDato)
		while opSbMenu != 99:
			lst.listar()
			resp = str (input("Desea Modificar Otro Dato: s/n? "))
			if resp == "s":
				opSbMenu = 0
				lDato = str(input("Ingrese el dato a Modificar: "))
				bDato = str(input("Ingrese el nuevo Dato: "))
				lst.modificar(lDato,bDato)
			elif resp == "S":
				opSbMenu = 0
				lDato = str(input("Ingrese el dato a Modificar: "))
				bDato = str(input("Ingrese el nuevo Dato: "))
				lst.modificar(lDato,bDato)
			else:
				opSbMenu = 99


def EliminarInicio():
	os.system(var) 
	print ("""
*****************************************************************
***************  Eliminar al primero de la lista  ***************
*****************************************************************
""")
	lst.listavacia()
	input("Presione una tecla para continura\n")
	lst.eliminar_inicio()
	lst.listar()
	input("Presione una tecla para continura\n")


def EliminarFin():
	os.system(var) 
	print ("""
*****************************************************************
***************  Eliminar al ultimo de la lista   ***************
*****************************************************************
""")
	lst.listar()
	input("Presione una tecla para continura\n")
	lst.eliminar_fin()
	lst.listar()
	input("Presione una tecla para continura\n")


def Eliminar_uno():
	os.system(var)	
	print ("""
*****************************************************************
***************   Eliminar un dato de la lista.   ***************
*****************************************************************
""")
	lDato =""
	if lst.listavacia() == True:
		print("La lista esta vacia \n")
		input("Presione una tecla para continuar: ")
	else:
		lst.listar()
		opSbMenu = 0
		lDato = str(input("Ingrese el dato a eliminar: "))
		lst.eliminar_uno(lDato)
		while opSbMenu != 99:
			lst.listar()
			resp = str (input("Desea Elimiar Otro Dato: s/n? "))
			if resp == "s":
				opSbMenu = 0
				lDAto = str(input("Ingrese el dato a eliminar: "))
				lst.eliminar_uno(lDato)
			elif resp == "S":
				opSbMenu = 0
				lDAto = str(input("Ingrese el dato a eliminar: "))
				lst.eliminar_uno(lDato)
			else:
				opSbMenu = 99
		#lst.listar()	

def VaciarLista():	
	os.system(var) 
	print ("""
*****************************************************************
***************   Eliminando datos de la lista.   ***************
*****************************************************************
""")	
	lst.vaciar()
	#time.sleep(2)
	input("Presione una tecla para continura\n")

def Menu():
	os.system(var) 
	opMenu = 0
	
	while opMenu != 99:
		os.system(var)
		
		print ("*****************************************************")
		print ("***   Menu Principal Lista Simplemente Enlazada   ***")
		print ("******************************************************")
		print ("                Seleccione Opcion")
		print ("1 -> Agregar Al Inicio")
		print ("2 -> Agregar Al Final")
		print ("3 -> Listar")
		print ("4 -> Modificar Registro")
		print ("5 -> Eliminar Inicio")
		print ("6 -> Eliminar Fin")	
		print ("7 -> Eliminar Un Dato")		
		print ("8 -> Vaciar Lista")
		print ("99 -> Salir \n")

		opMenu = int (input("Seleccione Opcion: "))
		#print(opMenu)

		if opMenu == 1: #Agregar un registro al inicio de la lista
			AgregarInicio()
		elif opMenu == 2:# Agregar un Registr al final de la lista
			AgregarFin()
		elif opMenu == 3:#recorrer y mostrar todos los datos
			Recorrer() 
		elif opMenu == 4:#Modifica un dato dentro de la lista
			ModificarDato()
		elif opMenu == 5:#Elimina el inicio de la lista
			EliminarInicio()
		elif opMenu == 6:#Elimina el final de la lista
			EliminarFin()
		elif opMenu == 7:
			Eliminar_uno()	
		elif opMenu == 8:#vacia la lista
			VaciarLista()
		#elif opMenu == 99:#Sale del sistema
		#	Salir()

Menu()