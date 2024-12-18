class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Lista:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        """Verifica si la lista está vacía."""
        return self.cabeza is None

    def agregar(self, dato):
        """Agrega un nodo al final de la lista."""
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def agregar_inicio(self, dato):
        """Agrega un nodo al inicio de la lista."""
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar(self, indice):
        """Elimina un nodo en una posición específica."""
        if self.esta_vacia():
            raise IndexError("La lista está vacía.")
        if indice == 0:
            eliminado = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            return eliminado

        actual = self.cabeza
        anterior = None
        contador = 0

        while actual and contador < indice:
            anterior = actual
            actual = actual.siguiente
            contador += 1

        if actual is None:
            raise IndexError("Índice fuera de rango.")

        eliminado = actual.dato
        anterior.siguiente = actual.siguiente
        return eliminado

    def vaciar(self):
        """Vacía toda la lista."""
        self.cabeza = None

    def mostrar(self):
        """Devuelve los elementos de la lista como una lista de Python."""
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos
