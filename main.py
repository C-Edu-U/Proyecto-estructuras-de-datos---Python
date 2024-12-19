import tkinter as tk
from presentacion.gui_pila import PilaGUI
from presentacion.gui_cola import ColaGUI
from presentacion.gui_lista import ListaGUI
from presentacion.gui_lista_doble import ListaDobleGUI


def main_menu(root):
    root.title("Menú Principal")
    tk.Label(root, text="Estructuras de Datos", font=("Arial", 18)).pack(pady=20)

    tk.Button(root, text="Operar con Pila", command=lambda: PilaGUI(root), width=20).pack(pady=10)
    tk.Button(root, text="Operar con Cola", command=lambda: ColaGUI(root), width=20).pack(pady=10)
    tk.Button(root, text="Operar con Lista", command=lambda: ListaGUI(root), width=20).pack(pady=10)
    tk.Button(root, text="Operar con Lista Doble", command=lambda: ListaDobleGUI(root), width=20).pack(pady=10)
    tk.Button(root, text="Salir", command=root.quit, width=20).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    main_menu(root)
    root.mainloop()
