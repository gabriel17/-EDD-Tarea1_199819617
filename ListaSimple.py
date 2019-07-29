from Nodo import Nodo
class ListaSimple():

	def __init__(self):
		self.inicio = None
		self.fin = None

	def listavacia(self):
		return self.inicio == None

	def insertar_inicio(self, lDato):
		xNodo = Nodo(lDato)
		if self.listavacia() == True:
			self.inicio =  xNodo
			self.fin = xNodo
		else:
			xNodo.siguiente = self.inicio
			self.inicio = xNodo

	def insertar_fin(self, lDato):
		xNodo = Nodo(lDato)
		if self.listavacia() == True:
			self.inicio = xNodo
			self.fin = xNodo
		else:
			self.fin.siguiente = xNodo
			self.fin = xNodo

	def eliminar_inicio(self):
		if self.listavacia() == False:
			print("Eliminando el dato " + self.inicio.dato)
			xNodo = self.inicio.siguiente
			self.inicio = xNodo			
		else:
			print("La Lista esta vacia \n\n")
		print("\n\n")

	def eliminar_fin(self):
		if self.listavacia() == False:
			xNodo = self.inicio
			while xNodo.siguiente != self.fin:
				xNodo = xNodo.siguiente
			xNodo.siguiente = None
			self.fin = xNodo
		else:
			print("La Lista esta vacia")

	def eliminar_uno(self,lDato):
		if self.listavacia() == True:
			print("La Lista esta vacia \n\n")
		else:
			print("Dato a eliminar: " + lDato)			
			if self.inicio.dato == lDato:
				self.eliminar_inicio();
			elif self.fin.dato == lDato:
				self.eliminar_fin()
			else:
				xNodo = self.inicio	
				while xNodo != self.fin:
					axNodo = xNodo
					if xNodo.siguiente != None:						
						if xNodo.siguiente.dato == lDato:
							axNodo = xNodo.siguiente
							xNodo.siguiente = axNodo.siguiente
							axNodo.siguiente = None
						else:
							xNodo = xNodo.siguiente
					
	def vaciar(self):
		if self.listavacia() == True:
			print("La Lista esta vacia \n\n")
		else:
			#xNodo = self.inicio
			while self.listavacia() == False:
				self.eliminar_inicio()

	def listar(self):
		xNodo = self.inicio
		#x = 0
		if self.listavacia() == True:
			print("La Lista esta vacia \n\n")
		else:	
			print("Vamos a obtener los datos:\n")
			while xNodo != None:			
				print (xNodo.dato)
				xNodo = xNodo.siguiente 
		print("\n\n")

	def modificar(self,xDato, xNuevoDato):
		if self.listavacia() ==True:
			print("La Lista esta vacia\n\n")
		else:
			if self.inicio.dato == xDato:
				self.inicio.dato = xNuevoDato 
			elif self.fin.dato == xDato:
				self.fin.dato = xNuevoDato
			else:
				xNodo = self.inicio
				print("va a entrar al while")
				while xNodo.siguiente != None:
					print("entro en el while")
					if xNodo.dato == xDato:
						xNodo.dato = xNuevoDato
					xNodo = xNodo.siguiente


