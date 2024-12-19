import time

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoble:
    def __init__(self):
        self.puntero = None

    def insertar_derecha(self, dato):
        """Inserta un nodo a la derecha del puntero."""
        nuevo = NodoDoble(dato)
        if self.puntero is None:
            self.puntero = nuevo
            self.puntero.siguiente = self.puntero
            self.puntero.anterior = self.puntero
        else:
            siguiente = self.puntero.siguiente
            nuevo.anterior = self.puntero
            nuevo.siguiente = siguiente
            self.puntero.siguiente = nuevo
            siguiente.anterior = nuevo

    def insertar_izquierda(self, dato):
        """Inserta un nodo a la izquierda del puntero."""
        nuevo = NodoDoble(dato)
        if self.puntero is None:
            self.puntero = nuevo
            self.puntero.siguiente = self.puntero
            self.puntero.anterior = self.puntero
        else:
            anterior = self.puntero.anterior
            nuevo.siguiente = self.puntero
            nuevo.anterior = anterior
            self.puntero.anterior = nuevo
            anterior.siguiente = nuevo

    def eliminar(self):
        """Elimina el nodo en la posición del puntero."""
        if self.puntero is None:
            return False  # Lista vacía
        if self.puntero.siguiente == self.puntero:  # Un solo nodo
            self.puntero = None
        else:
            anterior = self.puntero.anterior
            siguiente = self.puntero.siguiente
            anterior.siguiente = siguiente
            siguiente.anterior = anterior
            self.puntero = siguiente
        return True

    def mover_derecha(self):
        """Mueve el puntero a la derecha."""
        if self.puntero:
            self.puntero = self.puntero.siguiente

    def mover_izquierda(self):
        """Mueve el puntero a la izquierda."""
        if self.puntero:
            self.puntero = self.puntero.anterior

    def obtener_puntero(self):
        """Obtiene el dato del nodo actual."""
        return self.puntero.dato if self.puntero else None

    def limpiar(self):
        """Limpia la lista."""
        self.puntero = None

    def mostrar(self):
        """Devuelve una representación de la lista desde el puntero."""
        if self.puntero is None:
            return "Lista vacía."
        resultado = []
        actual = self.puntero
        while True:
            if actual == self.puntero:
                resultado.append(f"[{actual.dato}]")
            else:
                resultado.append(str(actual.dato))
            actual = actual.siguiente
            if actual == self.puntero:
                break
        return " <-> ".join(resultado)

    def sortear(self, vueltas, delay):
        """Realiza un sorteo simulando una ruleta.
        
        Args:
            vueltas (int): Número de movimientos en la ruleta.
            delay (float): Tiempo en segundos entre cada movimiento.
        """
        if self.puntero is None:
            return "Lista vacía. No se puede sortear."
        
        for _ in range(vueltas):
            self.mover_derecha()
            print(self.mostrar())  # Simula visualización en consola
            time.sleep(delay)
        
        return f"Ganador: {self.obtener_puntero()}"
