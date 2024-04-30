import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx


#Se crea grafo
grafo = nx.Graph()

#Se crea funcion que dibujará el grafo
def nuevoGrafo():
    ax.set_visible(True)
    ax.clear()
    pos = nx.spring_layout(grafo)
#Se asignan los parámetros que tendrá el grafo
    nx.draw(grafo, pos, with_labels=True, node_size=650, node_color="#5DD8CC", font_size=16, font_color="black", ax=ax) 
    ax.set_xticks([])
    ax.set_yticks([])
    espacio.draw()

#Se crea función para agregar vertice
def nuevoVertice(nombre_vertice):
    grafo.add_node(nombre_vertice)
    nuevoGrafo()


#Se crea función para agregar aristas
def nuevaArista(arista):
   #Se especifica la forma en la que se debe de ingresar la arista 
    vertice = arista.split("-")
    if len(vertice) != 2:
        messagebox.showerror("Error", "Separar los vertice con - para poder generar aristas")
        return
    v1, v2 = vertice
    if v1 not in grafo.nodes or v2 not in grafo.nodes:
        messagebox.showerror("Error", "Verificar que existan los vértices")
        return
    grafo.add_edge(v1, v2)
    nuevoGrafo()

#Se crea función para agregar vertice y aristas
def add():
    nuevo = entry.get()
    if nuevo:
        elementos = nuevo.split(",")
        for elemento in elementos:
            if "-" in elemento:
                nuevaArista(elemento)
            else:
                nuevoVertice(elemento)
        entry.delete(0, tk.END) 


#Funcion para el algoritmo de busqueda a anchura
def ancho():
    if not grafo:
        messagebox.showerror("Error", "Debe de ingresar el grafo para aplicar el algoritmo de búsqueda")
        return
    # Creaa una un segundo grafo para mostrar el resultado a lo ancho
    GrafoAncho = grafo.copy()
    # Aplicar el algoritmo de búsqueda en anchura
    AlgAncho = nx.bfs_tree(GrafoAncho, source=list(GrafoAncho.nodes)[0])
     #Ordena de forma ascendente los nodos
    ordenar = sorted(GrafoAncho.nodes())
     #Se dibuja el resultado
    pos = nx.spring_layout(AlgAncho)
    AlgAx.clear()
    #Se asignan los parámetros del grafo a anchura
    nx.draw(AlgAncho, pos,  nodelist=ordenar, with_labels=True, node_size=300, node_color="#87CF79", font_size=10, font_color="white", font_weight="bold", ax=AlgAx)
    AlgAx.set_visible(True)
    AlgAx.set_xticks([])
    AlgAx.set_yticks([])
    espacioR.draw()


    

#Se crea funcion para aplicar el algortimo de busqueda a lo largo
def largo():
    if not grafo:
        messagebox.showerror("Error", "Debe de ingresar el grafo para aplicar el algoritmo de búsqueda")
        return

  # Creaa una un segundo grafo para mostrar el resultado a lo largo
    GrafoLargo = grafo.copy()
    #Se aplica el algorithm de busqueda a lo largo
    AlgLargo = nx.dfs_tree(GrafoLargo, source=list(GrafoLargo.nodes)[0])
    #Se ordenan los nodos
    ordenar = sorted(GrafoLargo.nodes())
    #Se dibuja el resultado
    pos = nx.spring_layout(AlgLargo)
    AlgAx.clear()
    nx.draw(AlgLargo, pos, nodelist=ordenar, with_labels=True, node_size=300, node_color="#87CF79", font_size=10, font_color="white", font_weight="bold", ax=AlgAx)
    AlgAx.set_visible(True)
    AlgAx.set_xticks([])
    AlgAx.set_yticks([])
    espacioR.draw()



#Se crea la ventana inicial
ventana1 = tk.Tk()
ventana1.title("Proyecto Final Mate Para Computacion 1 - Grupo 6")
ventana1.geometry("1000x600")
ventana1.configure(bg="#79DDC6")

#Se crea frame
JFrame = tk.Frame(ventana1, bg="#79DDC6")
JFrame.pack(fill=tk.BOTH, expand=True)

#Se crea espacio donde se dibujará el grafo inicial
espacio = FigureCanvasTkAgg(plt.figure(figsize=(4, 4), facecolor="#79DDC6"), master=JFrame)
espacio.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
espacioResultado = tk.Frame(ventana1, bg="#79DDC6")
espacioResultado.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
Figura = plt.figure(figsize=(4, 4), facecolor="#79DDC6")
AlgAx = Figura.subplots()
AlgAx.set_visible(False)
espacioR = FigureCanvasTkAgg(Figura, master=espacioResultado)
espacioR.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


#Se crea frame para las funcionalidades
JFrameBtn = tk.Frame(ventana1, bg="#967D3A")
JFrameBtn.pack(fill="both", expand=1)
JFrameBtn.config(width=480,height=420) 

xd = tk.Label(JFrameBtn, text="Para generar los vertice, debe de ingresas la letra que este llevará, \n y para las aristas deberá de ingresar 2 vértices y separarlos por una coma", bg="#79DDC6", fg="white")
xd.pack()
entry = tk.Entry(JFrameBtn, width=40, bg="white", fg="#6B1717")
entry.place(x=5,y=58)

#Boton para generar vertice y aristas
btnAgregar = tk.Button(JFrameBtn, text="Añadir vertice o aristas", command=add, bg="#79B5CF", fg="white", padx=10)
btnAgregar.place(x=255, y=55)

#Boton pa generar a lo ancho
btnAncho = tk.Button(JFrameBtn, text="Búsqueda a lo ancho", command=ancho, bg="#87CF79", fg="white", padx=10)
btnAncho.place(x=45,y=90)

#Boton pa generar a lo largo
btnLargo = tk.Button(JFrameBtn, text="Búsqueda a lo largo", command=largo, bg="#87CF79", fg="white", padx=10)
btnLargo.place(x=200, y=90)


ax = espacio.figure.subplots()
ax.set_visible(False)



ventana1.mainloop()


