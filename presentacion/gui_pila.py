import tkinter as tk
from tkinter import messagebox
from negocios.pila import Pila


class PilaGUI:
    def __init__(self, root):
        self.pila = Pila()

        self.window = tk.Toplevel(root)
        self.window.title("Operar con Pila")

        # Elementos GUI
        tk.Label(self.window, text="Operaciones con Pila", font=("Arial", 16)).pack(pady=10)

        self.entry_elemento = tk.Entry(self.window, width=30)
        self.entry_elemento.pack(pady=5)
        tk.Button(self.window, text="Agregar", command=self.agregar_elemento).pack(pady=5)

        tk.Button(self.window, text="Sacar", command=self.sacar_elemento).pack(pady=5)
        tk.Button(self.window, text="Vaciar", command=self.vaciar_pila).pack(pady=5)
        tk.Button(self.window, text="Verificar si está vacía", command=self.verificar_vacia).pack(pady=5)

        self.text_area = tk.Text(self.window, width=50, height=10, state=tk.DISABLED)
        self.text_area.pack(pady=10)

        tk.Button(self.window, text="Cerrar", command=self.window.destroy).pack(pady=5)

    def agregar_elemento(self):
        elemento = self.entry_elemento.get()
        if elemento:
            self.pila.agregar(elemento)
            self.mostrar_pila()
            self.entry_elemento.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "El campo está vacío.")

    def sacar_elemento(self):
        elemento = self.pila.sacar()
        if elemento is not None:
            messagebox.showinfo("Elemento sacado", f"Elemento '{elemento}' sacado de la pila.")
        else:
            messagebox.showwarning("Pila vacía", "No hay elementos en la pila.")
        self.mostrar_pila()

    def vaciar_pila(self):
        self.pila.vaciar()
        self.mostrar_pila()

    def verificar_vacia(self):
        if self.pila.esta_vacia():
            messagebox.showinfo("Pila vacía", "La pila está vacía.")
        else:
            messagebox.showinfo("Pila no vacía", "La pila contiene elementos.")

    def mostrar_pila(self):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "Pila actual:\n")

        # Recorrer la pila y mostrar los elementos (desde el último al primero)
        nodo_actual = self.pila.cima
        while nodo_actual is not None:
            self.text_area.insert(tk.END, f"{nodo_actual.dato}\n")
            nodo_actual = nodo_actual.siguiente

        self.text_area.config(state=tk.DISABLED)

