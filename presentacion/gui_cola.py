import tkinter as tk
from tkinter import messagebox
from negocios.cola import Cola


class ColaGUI:
    def __init__(self, root):
        self.cola = Cola()

        self.window = tk.Toplevel(root)
        self.window.title("Operar con Cola")

        # Elementos GUI
        tk.Label(self.window, text="Operaciones con Cola", font=("Arial", 16)).pack(pady=10)

        self.entry_elemento = tk.Entry(self.window, width=30)
        self.entry_elemento.pack(pady=5)
        tk.Button(self.window, text="Agregar", command=self.agregar_elemento).pack(pady=5)

        tk.Button(self.window, text="Sacar", command=self.sacar_elemento).pack(pady=5)
        tk.Button(self.window, text="Vaciar", command=self.vaciar_cola).pack(pady=5)
        tk.Button(self.window, text="Verificar si está vacía", command=self.verificar_vacia).pack(pady=5)

        self.text_area = tk.Text(self.window, width=50, height=10, state=tk.DISABLED)
        self.text_area.pack(pady=10)

        tk.Button(self.window, text="Cerrar", command=self.window.destroy).pack(pady=5)

    def agregar_elemento(self):
        elemento = self.entry_elemento.get()
        if elemento:
            self.cola.agregar(elemento)
            self.mostrar_cola()
            self.entry_elemento.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "El campo está vacío.")

    def sacar_elemento(self):
        elemento = self.cola.sacar()
        if elemento is not None:
            messagebox.showinfo("Elemento sacado", f"Elemento '{elemento}' sacado de la cola.")
        else:
            messagebox.showwarning("Cola vacía", "No hay elementos en la cola.")
        self.mostrar_cola()

    def vaciar_cola(self):
        self.cola.vaciar()
        self.mostrar_cola()

    def verificar_vacia(self):
        if self.cola.esta_vacia():
            messagebox.showinfo("Cola vacía", "La cola está vacía.")
        else:
            messagebox.showinfo("Cola no vacía", "La cola contiene elementos.")

    def mostrar_cola(self):
        # Actualiza el contenido de la cola en el área de texto
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "Cola actual:\n")

        # Recorrer la cola y mostrar los elementos
        nodo_actual = self.cola.primero
        while nodo_actual is not None:
            self.text_area.insert(tk.END, f"{nodo_actual.valor}\n")
            nodo_actual = nodo_actual.siguiente

        self.text_area.config(state=tk.DISABLED)
