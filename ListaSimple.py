from Nodo import Nodo
class ListaSimple():

	def __init(self):
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
			self.fin.siguiente = xNodo.siguiente
			self.fin = xNodo

	def eliminar_inicio(self):
		if self.listavacia() == False:
			xNono = self.inicio.siguiente
			self.inicio = xNodo			
		else:
			print("La Lista esta vacia")


	def eliminar_fin(self):
		if self.listavacia() == False:
			xNodo = self.inicio
			while xNodo.siguiente != self.fin:
				xNodo = xNodo.siguiente
			xNodo.siguiente = None
			self.fin + xNodo
		else:
			print("La Lista esta vacia")

	def vaciar(self):
		if self.listavacia() == True:
			print("La Lista esta vacia")
		else:
			while self.listavacia() == False:
				self.eliminar_inicio()


	def listar(self):
		xNodo = self.inicio
		while xNodo != None:
			print (xNodo(dato))
			xNodo = xNodo.siguiente 

	def modificar(self,xDato, xNuevoDato):
		if self.listavacia() ==True:
			print("La Lista esta vacia")
		else:
			xNodo = self.inicio
			while xNodo.siguiente != None:
				if xNodo.dato == xDato:
					xNodo.dato = xNuevoDato

				xNodo = xNodo.siguiente


