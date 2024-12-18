import tkinter as tk
from tkinter import messagebox
from negocios.lista import Lista


class ListaGUI:
    def __init__(self, root):
        self.lista = Lista()

        self.window = tk.Toplevel(root)
        self.window.title("Operar con Lista")

        # Elementos GUI
        tk.Label(self.window, text="Operaciones con Lista", font=("Arial", 16)).pack(pady=10)

        self.entry_elemento = tk.Entry(self.window, width=30)
        self.entry_elemento.pack(pady=5)
        tk.Button(self.window, text="Agregar", command=self.agregar_elemento).pack(pady=5)

        tk.Button(self.window, text="Eliminar por índice", command=self.eliminar_elemento).pack(pady=5)
        tk.Button(self.window, text="Vaciar", command=self.vaciar_lista).pack(pady=5)
        tk.Button(self.window, text="Verificar si está vacía", command=self.verificar_vacia).pack(pady=5)

        self.text_area = tk.Text(self.window, width=50, height=10, state=tk.DISABLED)
        self.text_area.pack(pady=10)

        tk.Button(self.window, text="Cerrar", command=self.window.destroy).pack(pady=5)

    def agregar_elemento(self):
        elemento = self.entry_elemento.get()
        if elemento:
            self.lista.agregar(elemento)
            self.mostrar_lista()
            self.entry_elemento.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "El campo está vacío.")

    def eliminar_elemento(self):
        try:
            indice = int(self.entry_elemento.get())
            eliminado = self.lista.eliminar(indice)
            messagebox.showinfo("Elemento eliminado", f"Elemento '{eliminado}' eliminado de la lista.")
            self.mostrar_lista()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un índice válido.")
        except IndexError:
            messagebox.showwarning("Índice fuera de rango", "El índice proporcionado no es válido.")

    def vaciar_lista(self):
        self.lista.vaciar()
        self.mostrar_lista()

    def verificar_vacia(self):
        if self.lista.esta_vacia():
            messagebox.showinfo("Lista vacía", "La lista está vacía.")
        else:
            messagebox.showinfo("Lista no vacía", "La lista contiene elementos.")

    def mostrar_lista(self):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "Lista actual:\n")

        # Recorrer la lista y mostrar los elementos
        nodo_actual = self.lista.cabeza
        while nodo_actual is not None:
            self.text_area.insert(tk.END, f"{nodo_actual.dato}\n")
            nodo_actual = nodo_actual.siguiente

        self.text_area.config(state=tk.DISABLED)

