from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os
app = FastAPI()
# ---------------- CORS ----------------
origins = ["*"] # permitir cualquier origen
app.add_middleware(
 CORSMiddleware,
 allow_origins=origins,
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)
# --------------------------------------

FILE = "asistencia.xlsx"
# crear archivo si no existe
if not os.path.exists(FILE):
 df = pd.DataFrame(columns=["Nombre", "Materia", "Fecha"])
 df.to_excel(FILE, index=False)
@app.get("/form", response_class=HTMLResponse)
def form_assist():
  return """
  <html>
    <head>
      <title>Formulario de Asistencia</title>
    </head>
    <body>
      <h2>Registro de Asistencia</h2>
      <form action="/guardar" method="post">
        <label>Nombre:</label><br>
        <input type="text" name="nombre" required><br><br>
        <label>Materia:</label><br>
        <input type="text" name="materia" required><br><br>
        <label>Fecha:</label><br>
        <input type="date" name="fecha" required><br><br>
        <button type="submit">Enviar</button>
      </form>
    </body>
  </html>
  """

@app.post("/guardar")
def guardar(nombre: str = Form(...), materia: str = Form(...), fecha: str = Form(...)):
  df = pd.read_excel(FILE)

  nuevo = {
    "Nombre": nombre,
    "Materia": materia,
    "Fecha": fecha
  }

  df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)
  df.to_excel(FILE, index=False)

  return {"message": "Asistencia guardada"}

@app.get("/descargar")
def descargar_excel():
  return FileResponse(
    FILE,
    media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    filename="asistencia.xlsx"
  )
