# Proyecto Pila, Cola y Lista en Python

Este proyecto implementa tres estructuras de datos fundamentales: **pila** (LIFO), **cola** (FIFO) y **lista** (secuencial), con una interfaz gráfica básica desarrollada en **Tkinter** para la interacción del usuario.

## Descripción
El programa permite gestionar tres estructuras de datos (pila, cola y lista), ofreciendo operaciones comunes como agregar, eliminar y mostrar elementos. También muestra visualmente el estado actual de cada estructura.

## Funcionalidades
1. **Pila (LIFO - Last In, First Out):**
   - Agregar elementos.
   - Eliminar elementos (último en entrar es el primero en salir).
   - Vaciar la pila.
   - Mostrar los elementos actuales.

2. **Cola (FIFO - First In, First Out):**
   - Agregar elementos.
   - Eliminar elementos (primero en entrar es el primero en salir).
   - Vaciar la cola.
   - Mostrar los elementos actuales.

3. **Lista (secuencial):**
   - Agregar elementos al final de la lista.
   - Eliminar un elemento específico.
   - Verificar si la lista está vacía.
   - Mostrar los elementos actuales.

4. **Interfaz gráfica:**
   - Uso de **Tkinter** para proporcionar un entorno interactivo.
   - Botones para cada operación y cuadros de texto para ingresar datos.
   - Áreas de texto para visualizar los datos en tiempo real.

## Tecnologías utilizadas
- **Lenguaje:** Python 3.8 o superior.
- **Bibliotecas:**
  - **Tkinter:** Para la creación de la interfaz gráfica.

## Requisitos
- **Python:** 3.8 o superior.
- **Sistema operativo:** Compatible con Windows, macOS y Linux.

## Instalación y Ejecución
1. **Clonar o descargar el proyecto:**
   - Clona el proyecto desde el repositorio o descárgalo como un archivo ZIP.
2. **Instalar Python:**
   - Descarga e instala Python desde [python.org](https://www.python.org/).
3. **Ejecutar el programa:**
   - Abre una terminal o línea de comandos.
   - Navega a la carpeta del proyecto.
   - Ejecuta el archivo principal con:
     ```bash
     python main.py
     ```


## Estructura del proyecto
PilaColaApp/ 
├── negocios/ 
│   ├── pila.py # Lógica de la pila 
│   ├── cola.py # Lógica de la cola 
│   ├── lista.py # Lógica de la lista 
├── presentacion/ 
│   ├── gui_cola.py # Interfaz gráfica cola (Tkinter) 
│   ├── gui_pila.py # Interfaz gráfica pila (Tkinter) 
│   ├── gui_lista.py # Interfaz gráfica lista (Tkinter) 
├── main.py # Inicializador del programa 
├── README.md # Archivo de documentación

## Ejemplo de Uso
1. Abre la interfaz del programa con `main.py`.
2. Selecciona la estructura de datos que deseas operar (pila, cola o lista).
3. Realiza operaciones utilizando los botones y observa los cambios reflejados en el área de texto.

## Créditos
Desarrollado por Carlos Eduardo Ugarteche Virhuez. Si tienes dudas o comentarios, no dudes en contactarme.
