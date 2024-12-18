class Nodo:
    def __init__(self, valor):
        # Cada nodo tiene un valor y un enlace al siguiente nodo
        self.valor = valor
        self.siguiente = None


class Cola:
    def __init__(self):
        # Inicializa la cola con referencias al primer y último nodo como None
        self.primero = None
        self.ultimo = None

    def vaciar(self):
        # Vacía la cola reiniciándola
        self.primero = None
        self.ultimo = None

    def agregar(self, valor):
        # Crea un nuevo nodo con el valor dado
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            # Si la cola está vacía, el nuevo nodo es tanto el primero como el último
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            # Si no está vacía, enlaza el último nodo actual al nuevo nodo
            self.ultimo.siguiente = nuevo_nodo
            # Actualiza el último nodo de la cola
            self.ultimo = nuevo_nodo

    def sacar(self):
        # Remueve y devuelve el valor del primer nodo en la cola
        if not self.esta_vacia():
            valor = self.primero.valor
            # El primer nodo ahora será el siguiente en la cola
            self.primero = self.primero.siguiente
            if self.primero is None:  # Si no quedan más nodos, también actualiza el último
                self.ultimo = None
            return valor
        else:
            # Si la cola está vacía, devuelve None
            return None

    def esta_vacia(self):
        # Verifica si la cola está vacía
        return self.primero is None
