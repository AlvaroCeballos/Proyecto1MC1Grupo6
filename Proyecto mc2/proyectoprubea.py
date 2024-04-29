import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx

# Inicializar el grafo vacío
grafo = nx.Graph() 


def dibujar_grafo():
    ax.set_visible(True) 
    ax.clear()
    pos = nx.spring_layout(grafo) 
    nx.draw(grafo, pos, with_labels=True, node_size=650, node_color="#5DD8CC", font_size=17, font_color="black", ax=ax)
    ax.set_xticks([])
    ax.set_yticks([])
    canvas.draw()

def agregar_vertice(nombre_vertice):
    grafo.add_node(nombre_vertice)
    dibujar_grafo()

def agregar_arista(nombre_arista):
    vertices = nombre_arista.split("-")
    if len(vertices) != 2:
        messagebox.showerror("Error", "Debe ingresar exactamente dos vértices separados por un guión.")
        return
    nombre_vertice1, nombre_vertice2 = vertices
    if nombre_vertice1 not in grafo.nodes or nombre_vertice2 not in grafo.nodes:
        messagebox.showerror("Error", "Uno o ambos vértices ingresados no existen.")
        return
    grafo.add_edge(nombre_vertice1, nombre_vertice2)
    dibujar_grafo()

def agregar_elemento():
    entrada = entry.get()
    if entrada:
        elementos = entrada.split(",")
        for elemento in elementos:
            if "-" in elemento:
                agregar_arista(elemento)
            else:
                agregar_vertice(elemento)
        entry.delete(0, tk.END)  # Limpiar el contenido del Entry después de agregar elementos

def generar_grafo_ancho():
    if not grafo:
        messagebox.showerror("Error", "No hay grafo para generar.")
        return

    # Crear una copia del grafo original
    G_ancho = grafo.copy()
    # Aplicar el algoritmo de búsqueda en anchura
    grafo_ancho = nx.bfs_tree(G_ancho, source=list(G_ancho.nodes)[0])
    nodos_ordenados = sorted(G_ancho.nodes())
    # Dibujar el grafo en el segundo canvas
    pos = nx.spring_layout(grafo_ancho)
    ax_algoritmo.clear()
    nx.draw(grafo_ancho, pos, nodelist=nodos_ordenados, with_labels=True, node_size=300, node_color="#007acc", font_size=10, font_color="white", font_weight="bold", ax=ax_algoritmo)
    ax_algoritmo.set_visible(True)
    ax_algoritmo.set_xticks([])
    ax_algoritmo.set_yticks([])
    canvas_algoritmo.draw()

def generar_grafo_largo():
    if not grafo:
        messagebox.showerror("Error", "No hay grafo para generar.")
        return

    # Crear una copia del grafo original
    G_largo = grafo.copy()
    # Aplicar el algoritmo de búsqueda en profundidad
    grafo_largo = nx.dfs_tree(G_largo, source=list(G_largo.nodes)[0])
    nodos_ordenados = sorted(G_largo.nodes())
    # Dibujar el grafo en el segundo canvas
    pos = nx.spring_layout(grafo_largo)
    ax_algoritmo.clear()
    nx.draw(grafo_largo, pos, odelist=nodos_ordenados, with_labels=True, node_size=300, node_color="#007acc", font_size=10, font_color="white", font_weight="bold", ax=ax_algoritmo)
    ax_algoritmo.set_visible(True)
    ax_algoritmo.set_xticks([])
    ax_algoritmo.set_yticks([])
    canvas_algoritmo.draw()



# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Generador de Grafos Personalizado")
root.geometry("1000x600")
root.configure(bg="#2b2b2b")

frame_grafo = tk.Frame(root, bg="#2b2b2b")
frame_grafo.pack(fill=tk.BOTH, expand=True)

canvas = FigureCanvasTkAgg(plt.figure(figsize=(5, 5), facecolor="#2b2b2b"), master=frame_grafo) #
canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
canvas_algoritmos = tk.Frame(root, bg="#2b2b2b")
canvas_algoritmos.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

fig_algoritmo = plt.figure(figsize=(4, 4), facecolor="#2b2b2b")
ax_algoritmo = fig_algoritmo.subplots()
ax_algoritmo.set_visible(False)
canvas_algoritmo = FigureCanvasTkAgg(fig_algoritmo, master=canvas_algoritmos)
canvas_algoritmo.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

frame_botones = tk.Frame(root, bg="#2b2b2b")
frame_botones.pack(fill="both", expand=1)
frame_botones.config(width=480,height=420) 

label_instrucciones = tk.Label(frame_botones, text="Instrucciones:\nIngrese los vértices y aristas separados por comas y haga clic en 'Agregar Elemento'.\nUtilice el formato 'vertice' o 'vertice1-vertice2' para agregar vértices o aristas, respectivamente.", bg="#2b2b2b", fg="white")
label_instrucciones.pack()

entry = tk.Entry(frame_botones, width=40, bg="white", fg="#2b2b2b")
entry.place(x=5,y=58)

button_agregar_elemento = tk.Button(frame_botones, text="Agregar Elemento", command=agregar_elemento, bg="#007acc", fg="white", padx=10)
button_agregar_elemento.place(x=255, y=55)

button_generar_ancho = tk.Button(frame_botones, text="Generar Grafo (Ancho)", command=generar_grafo_ancho, bg="#007acc", fg="white", padx=10)
button_generar_ancho.place(x=45,y=90)

button_generar_largo = tk.Button(frame_botones, text="Generar Grafo (Largo)", command=generar_grafo_largo, bg="#007acc", fg="white", padx=10)
button_generar_largo.place(x=200, y=90)

ax = canvas.figure.subplots() 
ax.set_visible(False) # Ocultar el gráfico al inicio



root.mainloop() 