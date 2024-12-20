import tkinter as tk
from tkinter import messagebox
from negocios.lista_doble import ListaDoble
import threading
import time
import random


class RuletaGUI:
    def __init__(self, root):
        self.lista_doble = ListaDoble()

        self.window = tk.Toplevel(root)
        self.window.title("Ruleta con Lista Doble")

        # Configuración de la cinta
        self.canvas = tk.Canvas(self.window, width=500, height=100, bg="white")
        self.canvas.pack(pady=10)

        # Controles para la lista doble
        self.entry_elemento = tk.Entry(self.window, width=30)
        self.entry_elemento.pack(pady=5)

        tk.Button(self.window, text="Insertar Izquierda", command=self.insertar_izquierda).pack(pady=5)
        tk.Button(self.window, text="Insertar Derecha", command=self.insertar_derecha).pack(pady=5)
        tk.Button(self.window, text="Eliminar", command=self.eliminar).pack(pady=5)

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

        self.resultado_label = tk.Label(self.window, text="Premio: Ninguno", font=("Arial", 14))
        self.resultado_label.pack(pady=10)

        tk.Button(self.window, text="Cerrar", command=self.window.destroy).pack(pady=5)

        # Dibujar la lista inicial
        self.dibujar_cinta()

    def insertar_izquierda(self):
        elemento = self.entry_elemento.get()
        if elemento:
            self.lista_doble.insertar_izquierda(elemento)
            self.dibujar_cinta()
            self.entry_elemento.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "El campo está vacío.")

    def insertar_derecha(self):
        elemento = self.entry_elemento.get()
        if elemento:
            self.lista_doble.insertar_derecha(elemento)
            self.dibujar_cinta()
            self.entry_elemento.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "El campo está vacío.")

    def eliminar(self):
        if self.lista_doble.eliminar():
            self.dibujar_cinta()
        else:
            messagebox.showwarning("Lista vacía", "No hay elementos para eliminar.")

    def iniciar_sorteo(self):
        try:
            vueltas = int(self.entry_vueltas.get())
            delay = float(self.entry_delay.get())
            threading.Thread(target=self.ejecutar_ruleta, args=(vueltas, delay)).start()
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

    def ejecutar_ruleta(self, vueltas, delay):
        """Simula el giro de la ruleta moviendo la cinta gráficamente."""
        if self.lista_doble.puntero is None:
            messagebox.showwarning("Lista vacía", "No hay elementos para sortear.")
            return

        # Determinar el número total de movimientos con aleatoriedad
        longitud_lista = self.lista_doble.longitud()
        movimientos_totales = vueltas + random.randint(0, longitud_lista - 1)

        for _ in range(movimientos_totales):
            self.lista_doble.mover_derecha()
            self.dibujar_cinta(girar=True)
            time.sleep(delay)

        ganador = self.lista_doble.obtener_puntero()
        self.resultado_label.config(text=f"Premio: {ganador}")
        self.dibujar_cinta(girar=False)

    def dibujar_cinta(self, girar=False):
        """Dibuja la lista doble en el canvas, con efecto de giro."""
        self.canvas.delete("all")  # Limpiar el canvas

        if self.lista_doble.puntero is None:
            self.canvas.create_text(250, 50, text="Lista vacía.", font=("Arial", 16), fill="black")
            return

        # Configuración inicial
        x, y = 50, 50  # Posición inicial
        espacio = 100  # Espacio entre nodos

        # Efecto de giro
        if girar:
            x -= espacio  # Desplaza todo hacia la izquierda para simular rotación

        # Dibujar nodos de la lista
        actual = self.lista_doble.puntero
        for _ in range(self.lista_doble.longitud()):
            color = "red" if actual == self.lista_doble.puntero else "lightblue"
            self.canvas.create_rectangle(x, y - 20, x + 80, y + 20, fill=color, outline="black")
            self.canvas.create_text(x + 40, y, text=str(actual.dato), font=("Arial", 12), fill="black")
            actual = actual.siguiente
            x += espacio

        # Ajustar desplazamiento circular
        if girar:
            self.canvas.move("all", espacio, 0)

