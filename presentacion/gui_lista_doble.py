import tkinter as tk
from tkinter import messagebox
from negocios.lista_doble import ListaDoble


class ListaDobleGUI:
    def __init__(self, root):
        self.lista_doble = ListaDoble()

        self.window = tk.Toplevel(root)
        self.window.title("Operar con Lista Doble")

        # Elementos de la GUI
        tk.Label(self.window, text="Operaciones con Lista Doble", font=("Arial", 16)).pack(pady=10)

        self.entry_elemento = tk.Entry(self.window, width=30)
        self.entry_elemento.pack(pady=5)

        tk.Button(self.window, text="Insertar Izquierda", command=self.insertar_izquierda).pack(pady=5)
        tk.Button(self.window, text="Insertar Derecha", command=self.insertar_derecha).pack(pady=5)
        tk.Button(self.window, text="Eliminar", command=self.eliminar).pack(pady=5)
        tk.Button(self.window, text="Mover Izquierda", command=self.mover_izquierda).pack(pady=5)
        tk.Button(self.window, text="Mover Derecha", command=self.mover_derecha).pack(pady=5)
        tk.Button(self.window, text="Limpiar Lista", command=self.limpiar).pack(pady=5)

        self.text_area = tk.Text(self.window, width=50, height=10, state=tk.DISABLED)
        self.text_area.pack(pady=10)

        tk.Button(self.window, text="Cerrar", command=self.window.destroy).pack(pady=5)

    def insertar_izquierda(self):
        elemento = self.entry_elemento.get()
        if elemento:
            self.lista_doble.insertar_izquierda(elemento)
            self.mostrar_lista()
            self.entry_elemento.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "El campo está vacío.")

    def insertar_derecha(self):
        elemento = self.entry_elemento.get()
        if elemento:
            self.lista_doble.insertar_derecha(elemento)
            self.mostrar_lista()
            self.entry_elemento.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "El campo está vacío.")

    def eliminar(self):
        if self.lista_doble.eliminar():
            self.mostrar_lista()
        else:
            messagebox.showwarning("Lista vacía", "No hay elementos para eliminar.")

    def mover_izquierda(self):
        self.lista_doble.mover_izquierda()
        self.mostrar_lista()

    def mover_derecha(self):
        self.lista_doble.mover_derecha()
        self.mostrar_lista()

    def limpiar(self):
        self.lista_doble.limpiar()
        self.mostrar_lista()

    def mostrar_lista(self):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, self.lista_doble.mostrar())
        self.text_area.config(state=tk.DISABLED)
