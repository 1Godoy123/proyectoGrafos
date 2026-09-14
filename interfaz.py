import tkinter as tk
import math
import logica

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

    def click(self,e):
        v = self.buscarVertice(e.x,e.y)
        if  v is None:
            return
        if self.sel is None:
            self.sel = v
        else: 
            if self.sel != v:
                arista = (self.sel,v)
                if (arista not in self.aristas 
                and (v,self.sel) not in self.aristas):
                    self.aristas.append(arista)
            self.sel = None
        self.dibujarGrafo()

    def buscarVertice(self,x,y):  
        for v, (vx, vy) in self.pos.items():

            if math.hypot(x - vx, y - vy) <= 20:
                return v

        return None

    def entregarGrafo(self):
        resultado = logica.analizar(
            self.vertices,
            self.aristas
        )

        texto = "RESULTADO"

        texto += f"V = {self.vertices}\n"
        texto += f"A = {self.aristas}\n\n"

        texto += f"M = {resultado['M']}\n\n"

        texto += (
            f"Emparejamiento: "
            f"{resultado['emparejamiento']}\n"
        )

        texto += (
            f"Maximal: "
            f"{resultado['esMaximal']}\n"
        )

        texto += (
            f"Máximo: "
            f"{resultado['esMaximo']}\n"
        )

        texto += (
            f"Perfecto: "
            f"{resultado['esPerfecto']}\n"
        )

        resultado_ventana = tk.Toplevel()
        resultado_ventana.title("Resultado")

        tk.Label(
            resultado_ventana,
            text=texto,
            justify="left",
            padx=20,
            pady=20
        ).pack()
    
              
ventana = tk.Tk()
ventana.title("Proyecto de Grafos")
ventana.geometry("800x650")

Grafo(ventana)

ventana.mainloop()        