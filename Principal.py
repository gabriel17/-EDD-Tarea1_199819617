from ListaSimple import ListaSimple

def AgregarInicio():
	print ("Agregando en la lista al inicio")
def AgregarFin():
	print("Agregando al final de la lista")
def Recorrer():
	print("Reccorriendo la lista")
def ModificarDato():
	print("Modificar un dato existente")
def EliminarInicio():
	print("Eliminiar el inicio de la lista")
def EliminarFin():
	print("Eliminar el final de la lista")
def VaciarLista():
	print("Vanciando la lista")
def Salir():
	print("Saliendo del sistema...")
	exit()

def Menu():
	opMenu = 0
	
	while opMenu != 99:
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
		print ("7 -> Vaciar  Lista")
		print ("99 -> Salir")

		opMenu = input("Seleccione Opcion: ")

		if opMenu == 1: #Agregar un registro al inicio de la lista
			AgregarInicio()
		elif opMenu == 2:# Agregar un Registr al final de la lista
			AgregarFin()
		elif opMenu == 3:#recorrer y mostrar todos los datos
			Recorrer() 
		elif opMenu == 4:#Modifica un dato dentro de la lista
			ModificarDato()
		elif opMenu == 5:#Elimina el inicio de la lista
			EliminaInicio()
		elif opMenu == 6:#Elimina el final de la lista
			EliminaFin()
		elif opMenu == 7:#vacia la lista
			VaciarLista()
		elif opMenu == 99:#Sale del sistema
			Salir()

Menu()


