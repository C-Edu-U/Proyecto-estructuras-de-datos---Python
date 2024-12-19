import tkinter as tk
from tkinter import messagebox
from math import pi, cos, sin
from negocios.lista_doble import ListaDoble
import random
import time


class RuletaGUI:
    def __init__(self, root):
        self.lista_doble = ListaDoble()
        self.window = tk.Toplevel(root)
        self.window.title("Ruleta Gráfica")

        # Configuración del Canvas para la ruleta
        self.canvas = tk.Canvas(self.window, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)

        # Controles para configurar la ruleta
        self.entry_vueltas = tk.Entry(self.window, width=10)
        self.entry_vueltas.insert(0, "30")
        self.entry_delay = tk.Entry(self.window, width=10)
        self.entry_delay.insert(0, "50")  # Milisegundos

        tk.Label(self.window, text="Vueltas:").pack(pady=2)
        self.entry_vueltas.pack(pady=2)
        tk.Label(self.window, text="Delay (ms):").pack(pady=2)
        self.entry_delay.pack(pady=2)

        tk.Button(self.window, text="Iniciar Sorteo", command=self.iniciar_sorteo).pack(pady=5)
        self.resultado_label = tk.Label(self.window, text="Resultado: Ninguno", font=("Arial", 14))
        self.resultado_label.pack(pady=10)

        # Entrada para agregar nodos
        self.entry_elemento = tk.Entry(self.window, width=20)
        self.entry_elemento.pack(pady=5)
        tk.Button(self.window, text="Agregar Nodo", command=self.agregar_nodo).pack(pady=5)

        # Botón para limpiar la lista
        tk.Button(self.window, text="Limpiar Lista", command=self.limpiar_lista).pack(pady=5)

        self.nodos = []  # Lista de nodos visibles
        self.angulo_inicio = 0  # Ángulo inicial de la ruleta

    def agregar_nodo(self):
        elemento = self.entry_elemento.get()
        if elemento:
            self.lista_doble.insertar_derecha(elemento)
            self.nodos.append(elemento)
            self.dibujar_ruleta()
            self.entry_elemento.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "El campo está vacío.")

    def limpiar_lista(self):
        self.lista_doble.limpiar()
        self.nodos.clear()
        self.dibujar_ruleta()

    def dibujar_ruleta(self):
        """Dibuja la ruleta circular en el canvas."""
        self.canvas.delete("all")  # Limpiar el canvas

        if not self.nodos:
            self.canvas.create_text(200, 200, text="Lista Vacía", font=("Arial", 16))
            return

        num_nodos = len(self.nodos)
        angulo_por_nodo = 360 / num_nodos  # Ángulo de cada segmento

        for i, nodo in enumerate(self.nodos):
            start_angle = self.angulo_inicio + i * angulo_por_nodo
            end_angle = start_angle + angulo_por_nodo

            # Dibujar el arco (segmento circular)
            self.canvas.create_arc(
                50, 50, 350, 350,
                start=start_angle,
                extent=angulo_por_nodo,
                fill=self.color_por_indice(i),
                outline="black"
            )

            # Coordenadas del texto
            mid_angle = start_angle + angulo_por_nodo / 2
            x = 200 + 100 * cos(mid_angle * pi / 180)
            y = 200 - 100 * sin(mid_angle * pi / 180)
            self.canvas.create_text(x, y, text=str(nodo), font=("Arial", 10), fill="white")

        # Dibujar el puntero
        self.canvas.create_polygon(
            190, 20, 210, 20, 200, 50, fill="red"
        )

    def color_por_indice(self, indice):
        """Devuelve un color para un índice dado."""
        colores = ["#FF5733", "#33FF57", "#3357FF", "#F0FF33", "#FF33A8"]
        return colores[indice % len(colores)]

    def iniciar_sorteo(self):
        try:
            vueltas = int(self.entry_vueltas.get())
            delay = int(self.entry_delay.get())
            ganador = random.choice(self.nodos) if self.nodos else "Ninguno"

            self.resultado_label.config(text="Girando...")
            self.girar_ruleta(vueltas, delay, ganador)
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

    def girar_ruleta(self, vueltas, delay, ganador):
        """Simula el giro de la ruleta y selecciona un ganador."""
        pasos = vueltas * len(self.nodos) + self.nodos.index(ganador)

        for _ in range(pasos):
            self.angulo_inicio = (self.angulo_inicio - 10) % 360
            self.dibujar_ruleta()
            self.window.update()
            time.sleep(delay / 1000)  # Delay en segundos

        self.resultado_label.config(text=f"Ganador: {ganador}")
