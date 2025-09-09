try:
    import os
    import sqlite3 as s3
    from pathlib import Path
    from tkinter import Tk, Label
    from PIL import Image, ImageTk
    import io
except ImportError as e:
    print('Error al importar la librería -->', e)

# Preparar ruta de la base de datos
folder_db = 'db/folder_db'
name_db = 'image.db'
name_db = str(Path(name_db).with_suffix('.db'))
full_path_db = os.path.join(folder_db, name_db)

# Crear carpeta si no existe
if not os.path.exists(folder_db):
    os.makedirs(folder_db)

# Conectarse a la base de datos
conn = s3.connect(full_path_db)
cr = conn.cursor()

# Crear la tabla si no existe
cr.execute('''
    CREATE TABLE IF NOT EXISTS images(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        image BLOB
    );
''')

# Leer la imagen desde disco
with open('./public/img.jpg', 'rb') as file:
    img_bytes = file.read()

# Insertar la imagen si la tabla está vacía
cr.execute('SELECT COUNT(*) FROM images')
if cr.fetchone()[0] == 0:
    cr.execute('INSERT INTO images (image) VALUES (?)', (img_bytes,))
    conn.commit()

# Recuperar la imagen
cr.execute('SELECT image FROM images WHERE id = 1')
result = cr.fetchone()
conn.close()

# Procesar la imagen
img_tk = None
if result:
    image_bytes = result[0]
    img = Image.open(io.BytesIO(image_bytes))
    
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    img_tk = ImageTk.PhotoImage(img)

# Mostrar la imagen en Tkinter
root = Tk()
root.title("Imagen desde SQLite")

if img_tk:
    label = Label(root, image=img_tk)
    label.image = img_tk  # Mantener referencia viva
    label.pack()
else:
    label = Label(root, text="No se pudo cargar la imagen.")
    label.pack()

root.mainloop()
