import tkinter as tk
from tkinter import messagebox
from negocios.lista_doble import ListaDoble
import threading

class RuletaGUI:
    def __init__(self, root):
        self.lista_doble = ListaDoble()

        self.window = tk.Toplevel(root)
        self.window.title("Ruleta con Lista Doble")

        # Elementos de la GUI
        tk.Label(self.window, text="Ruleta con Lista Doble", font=("Arial", 16)).pack(pady=10)

        self.entry_elemento = tk.Entry(self.window, width=30)
        self.entry_elemento.pack(pady=5)

        tk.Button(self.window, text="Insertar Izquierda", command=self.insertar_izquierda).pack(pady=5)
        tk.Button(self.window, text="Insertar Derecha", command=self.insertar_derecha).pack(pady=5)
        tk.Button(self.window, text="Eliminar", command=self.eliminar).pack(pady=5)

        self.text_area = tk.Text(self.window, width=50, height=10, state=tk.DISABLED)
        self.text_area.pack(pady=10)

        # Configuración de la ruleta
        self.entry_vueltas = tk.Entry(self.window, width=10)
        self.entry_vueltas.insert(0, "30")
        self.entry_delay = tk.Entry(self.window, width=10)
        self.entry_delay.insert(0, "0.1")
        
        tk.Label(self.window, text="Vueltas:").pack(pady=2)
        self.entry_vueltas.pack(pady=2)
        tk.Label(self.window, text="Delay (segundos):").pack(pady=2)
        self.entry_delay.pack(pady=2)

        tk.Button(self.window, text="Iniciar Sorteo", command=self.iniciar_sorteo).pack(pady=5)

        self.resultado_label = tk.Label(self.window, text="Resultado: Ninguno", font=("Arial", 14))
        self.resultado_label.pack(pady=10)

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

    def mostrar_lista(self):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, self.lista_doble.mostrar())
        self.text_area.config(state=tk.DISABLED)

    def iniciar_sorteo(self):
        try:
            vueltas = int(self.entry_vueltas.get())
            delay = float(self.entry_delay.get())
            threading.Thread(target=self.ejecutar_ruleta, args=(vueltas, delay)).start()
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

    def ejecutar_ruleta(self, vueltas, delay):
        resultado = self.lista_doble.sortear(vueltas, delay)
        self.resultado_label.config(text=resultado)
        self.mostrar_lista()
