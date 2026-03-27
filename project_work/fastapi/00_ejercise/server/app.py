from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from server.create_files import CreateFiles
import os
import json
import config as cg
from jinja2 import Environment, FileSystemLoader

app = FastAPI()

env = Environment(
    loader=FileSystemLoader(cg.template_path)
)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],  # en producción, especifica tu frontend
  allow_methods=["*"],
  allow_headers=["*"],
)

# Plantilla html
server_dir = os.path.dirname(__file__)
tmp = Jinja2Templates(directory=cg.template_path)

@app.get('/assistence')
def form_assistence(req: Request):
  try:
    with open(cg.file_json, "r", encoding="utf-8") as f:
      courses = json.load(f)
  except:
    courses = {'body': []}

  print(courses)

  return tmp.TemplateResponse("assistence.html", {
    "request": req,
    "courses": courses['body']
  })

@app.get('/courses')
def get_courses_page(req: Request):
  return tmp.TemplateResponse("course.html", {
    "request": req
  })

@app.post("/courses")
def get_courses_page(course: str = Form(...)):
  # Si no existe, lo creamos
  if not os.path.exists(cg.file_json):
    with open(cg.file_json, "w", encoding="utf-8") as f:
      json.dump({"body": []}, f, indent=4)

  # Leer cursos actuales
  with open(cg.file_json, "r", encoding="utf-8") as f:
    courses = json.load(f)

  # Si no es dict, inicializar correctamente
  if not isinstance(courses, dict):
    courses = {"body": []}

  # Evitar duplicados
  if course not in courses['body']:
    courses['body'].append(course)

  # Guardar
  with open(cg.file_json, "w", encoding="utf-8") as f:
    json.dump(courses, f, indent=4)

  return RedirectResponse(url="/courses?success=1", status_code=303)

@app.post("/assistence")
async def add_assistence(
  username: str = Form(...),
  lastname: str = Form(...),
  datetime: str = Form(...),
  course: str = Form(...)
):
  # select = cours
  CreateFiles.create_excel(
    course=course,
    data=[username, lastname, datetime, course]
  )

  return RedirectResponse(url="/assistence?success=1", status_code=303)