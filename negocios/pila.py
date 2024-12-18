class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None

    def esta_vacia(self):
        return self.cima is None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo

    def sacar(self):
        if self.esta_vacia():
            return None
        dato = self.cima.dato
        self.cima = self.cima.siguiente
        return dato

    def mostrar(self):
        elementos = []
        actual = self.cima
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

    def vaciar(self):
        # Vacía la pila reiniciándola
        self.cima = None
