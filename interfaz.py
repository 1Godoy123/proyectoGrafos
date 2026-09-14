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
        n = int(self.entrada.get())
        self.vertices = list(
            range(1,n+1)
        )
        self.aristas = []
        self.sel=None

        self.dibujarGrafo()

    def dibujarGrafo(self):
        self.canvas.delete("all")

        n = len(self.vertices)
        if n == 0:
            return
        cx =350
        cy =250
        r = 180

        for i, v in enumerate(self.vertices):

            a = 2 * math.pi * i / n - math.pi / 2

            self.pos[v] = (
                cx + r * math.cos(a),
                cy + r * math.sin(a)
            )

        for u, v in self.aristas:

            self.canvas.create_line(
                *self.pos[u],
                *self.pos[v],
                width=2
            )

        for v in self.vertices:

            x, y = self.pos[v]

            color = (
                "yellow"
                if v == self.sel
                else "lightblue"
            )        

            self.canvas.create_oval(
                x-20,
                y-20,
                x+20,
                y+20,
                fill=color
            )
            self.canvas.create_text(
                x, y,
                text=v
            )

    def entregarGrafo(self):
        return self.vertices, self.aristas
    def click(self,e):
        return self.entrada.get()

ventana = tk.Tk()
ventana.title("Proyecto de Grafos")
ventana.geometry("800x650")

Grafo(ventana)

ventana.mainloop()        