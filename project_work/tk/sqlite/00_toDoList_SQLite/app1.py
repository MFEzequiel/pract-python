import tkinter as tk
from tkinter import ttk, filedialog
import sqlite3
import os
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SQLiteBrowser:
  def __init__(self, root):
    self.root = root
    self.root.title("SQLite Browser")

    # Frames principales
    self.sidebar = tk.Frame(root, width=200, bg="#f0f0f0")
    self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

    self.main_panel = tk.Frame(root)
    self.main_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Botón para cargar base de datos
    self.load_btn = tk.Button(self.sidebar, text="Cargar DB", command=self.load_database)
    self.load_btn.pack(pady=10)

    # Árbol para mostrar DB y tablas
    self.tree = ttk.Treeview(self.sidebar)
    self.tree.pack(fill=tk.BOTH, expand=True)
    self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

    # Treeview para mostrar datos
    self.data_tree = ttk.Treeview(self.main_panel)
    self.data_tree.pack(fill=tk.BOTH, expand=True)

    # Canvas para mostrar gráfico
    self.graph_canvas_frame = tk.Frame(self.main_panel)
    self.graph_canvas_frame.pack(fill=tk.BOTH, expand=True)

    self.databases = {}  # ruta -> conexión

  def load_database(self):
    db_path = filedialog.askopenfilename(
       filetypes=[("SQLite files", "*.sqlite *.db")]
    )
    
    if db_path:
      db_name = os.path.basename(db_path)

      if db_path not in self.databases:
        conn = sqlite3.connect(db_path)
        self.databases[db_path] = conn

        db_node = self.tree.insert("", "end", text=db_name, open=True, values=[db_path])

        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        self.tables = cursor.fetchall()

        for table in self.tables:
          table_name = table[0]
          self.tree.insert(db_node, "end", text=table_name, values=[db_path, table_name])

  def on_tree_select(self, event):
    selected = self.tree.focus()
    values = self.tree.item(selected, "values")

    # Si es tabla (tiene nombre de tabla y db)
    if len(values) == 2:
      db_path, table_name = values
      self.conn = self.databases[db_path]
      cursor = self.conn.cursor()

      try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        # Limpiar el panel de datos
        for col in self.data_tree.get_children():
          self.data_tree.delete(col)
        self.data_tree.delete(*self.data_tree.get_children())

        self.data_tree["columns"] = columns
        self.data_tree["show"] = "headings"

        for col in columns:
          self.data_tree.heading(col, text=col)
          self.data_tree.column(col, anchor=tk.W)

        for row in rows:
          self.data_tree.insert("", "end", values=row)

        # Mostrar relaciones entre tablas
        self.display_table_graph()

      except sqlite3.Error as e:
        print("Error al leer tabla:", e)

  def display_table_graph2(self):
    import networkx as nx
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    graph = nx.DiGraph()
    cursor = self.conn.cursor()

    # Obtener todas las tablas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]

    # Añadir nodos (tablas)
    for table in tables:
      graph.add_node(table)

    # Añadir aristas según claves foráneas
    for table in tables:
      cursor.execute(f"PRAGMA foreign_key_list('{table}')")
      fkeys = cursor.fetchall()
      for fk in fkeys:
        ref_table = fk[2]  # Tabla referenciada
        graph.add_edge(table, ref_table)

    # Limpiar canvas anterior
    for widget in self.graph_canvas_frame.winfo_children():
      widget.destroy()

    # Crear figura y eje (orientado a objetos)
    fig, ax = plt.subplots(figsize=(6, 5))

    pos = nx.spring_layout(graph, seed=42)
    nx.draw(
      graph, pos, ax=ax,
      with_labels=True,
      node_size=2000,
      node_color="skyblue",
      font_size=10,
      font_weight="bold",
      edge_color="gray",
      arrows=True,
      arrowstyle="->"
    )
    ax.set_title("Relaciones entre Tablas")

    # Incrustar en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=self.graph_canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # No limpiar la figura para no borrar el gráfico
    # plt.clf()  <-- quita esta línea

  def display_table_graph3(self):
    import networkx as nx
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    graph = nx.DiGraph()
    cursor = self.conn.cursor()

    # Obtener todas las tablas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]

    # Añadir nodos (tablas)
    for table in tables:
      graph.add_node(table)

    # Añadir aristas con etiquetas (columnas relacionadas) según claves foráneas
    edge_labels = {}
    for table in tables:
      cursor.execute(f"PRAGMA foreign_key_list('{table}')")
      fkeys = cursor.fetchall()
      for fk in fkeys:
        ref_table = fk[2]  # Tabla referenciada
        from_col = fk[3]   # Columna en la tabla actual
        to_col = fk[4]     # Columna referenciada
        graph.add_edge(table, ref_table)
        edge_labels[(table, ref_table)] = f"{from_col} → {to_col}"

    # Limpiar canvas anterior
    for widget in self.graph_canvas_frame.winfo_children():
      widget.destroy()

    # Crear figura y eje (orientado a objetos)
    fig, ax = plt.subplots(figsize=(8, 6))

    pos = nx.spring_layout(graph, seed=42)
    nx.draw(
      graph, pos, ax=ax,
      with_labels=True,
      node_size=2000,
      node_color="skyblue",
      font_size=10,
      font_weight="bold",
      edge_color="gray",
      arrows=True,
      arrowstyle="->"
    )
    # nx.draw_networkx_edge_labels(ax, pos, edge_labels=edge_labels, font_color="red", font_size=9)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color="red", font_size=9, ax=ax)

    ax.set_title("Diagrama DDR: Relaciones y Dependencias entre Tablas")

    # Incrustar en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=self.graph_canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

  def display_table_graph(self):
    import networkx as nx
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import math

    graph = nx.DiGraph()
    cursor = self.conn.cursor()

    # Obtener todas las tablas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]

    # Detectar tablas puente (con 2 o más FKs)
    fk_counts = {}
    for table in tables:
        cursor.execute(f"PRAGMA foreign_key_list('{table}')")
        fkeys = cursor.fetchall()
        fk_counts[table] = len(fkeys)

    # Añadir nodos (tablas)
    for table in tables:
        label = table
        if fk_counts.get(table, 0) >= 2:
            label += "\n(Intermedia N:N)"
        graph.add_node(table, label=label)

    edge_labels = {}
    for table in tables:
        cursor.execute(f"PRAGMA foreign_key_list('{table}')")
        fkeys = cursor.fetchall()
        for fk in fkeys:
            ref_table = fk[2]  # Tabla referenciada
            from_col = fk[3]   # Columna en tabla actual
            to_col = fk[4]     # Columna en tabla referenciada

            # Verificar si from_col es UNIQUE o PK para determinar tipo relación
            cursor.execute(f"PRAGMA index_list('{table}')")
            indexes = cursor.fetchall()
            unique_cols = set()

            # Buscar columnas con índice UNIQUE
            for idx in indexes:
                idx_name = idx[1]
                is_unique = idx[2]
                if is_unique:
                    cursor.execute(f"PRAGMA index_info('{idx_name}')")
                    idx_info = cursor.fetchall()
                    for info in idx_info:
                        unique_cols.add(info[2])  # Nombre columna

            # Verificar PK columnas
            cursor.execute(f"PRAGMA table_info('{table}')")
            table_info = cursor.fetchall()
            pk_cols = set()
            for col in table_info:
                if col[5] == 1:  # pk = 1
                    pk_cols.add(col[1])

            # Determinar tipo de relación
            if from_col in unique_cols or from_col in pk_cols:
                relation = "1:1"
            else:
                relation = "1:N"

            # Construir etiqueta para arista
            label = f"{from_col} → {to_col}\n({relation})"
            graph.add_edge(table, ref_table)
            edge_labels[(table, ref_table)] = label

    # Limpiar canvas anterior
    for widget in self.graph_canvas_frame.winfo_children():
        widget.destroy()

    # Crear figura
    fig, ax = plt.subplots(figsize=(12, 7))

    # Layout en tabla (rejilla)
    cols = math.ceil(math.sqrt(len(tables)))
    pos = {}
    for i, table in enumerate(tables):
        row = i // cols
        col = i % cols
        pos[table] = (col * 3, -row * 3)

    # Dibujar nodos con etiquetas
    labels = nx.get_node_attributes(graph, 'label')
    nx.draw_networkx_nodes(graph, pos, node_size=2500, node_color="lightblue", ax=ax)
    nx.draw_networkx_labels(graph, pos, labels=labels, font_weight="bold", font_size=9, ax=ax)

    # Dibujar aristas y etiquetas
    nx.draw_networkx_edges(graph, pos, arrowstyle="->", arrowsize=20, edge_color="gray", ax=ax)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color="red", font_size=8, ax=ax)

    ax.set_title("Diagrama DDR con tipo de relación (1:1, 1:N, N:N)", fontsize=13)
    ax.axis("off")

    # Incrustar en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=self.graph_canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
  root = tk.Tk()
  root.geometry("800x600")
  app = SQLiteBrowser(root)
  root.mainloop()
