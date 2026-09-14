import tkinter as tk
import math

class Grafo:
    def __init__(self,ventana):
        self.vertices = []
        self.aristas = []
        self.pos ={}
        self.sel = None

        tk.Label(
            ventana,
            text="vertices:",
        ).pack()

        self.entrada = tk.Entry(ventana)
        self.entrada.pack()

        tk.Button(
            ventana,
            text="Crear grafo",
            command=self.crearGrafo
        ).pack()

        tk.Button(
            ventana,
            text="Entregar",
            command=self.entregarGrafo
        ).pack()        

        self.canvas = tk.Canvas(
            ventana,
            width=700,
            height=500,
            bg="white"
        )
        self.canvas.pack()

        self.canvas.bind(
            "<Button-1>",
            self.click
        )


    def crearGrafo(self):
        return self.entrada.get()

    def entregarGrafo(self):
        return self.vertices, self.aristas
    def click(self,e):
        return self.entrada.get()

ventana = tk.Tk()
ventana.title("Proyecto de Grafos")
ventana.geometry("800x650")

Grafo(ventana)

ventana.mainloop()        