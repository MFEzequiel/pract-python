# -*- coding: utf-8 -*-
try:
  import sqlite3
  from tkinter import Tk, scrolledtext, Label, Entry, StringVar, Button, WORD
  from db import manager
  from ui import menu
  from sklearn.feature_extraction.text import TfidfVectorizer
  from sklearn.metrics.pairwise import cosine_similarity
except ImportError as e:
  print('Error al inportar la libreria ', e)

class Root:
  def __init__(self) -> None:
    self.root = Tk()
    self.root.title('RAG básico con SQLite y scikit-learn')
    self.root.geometry('600x500')
    
    self.create_widgets()
    # self.load_documents()
    # self.build_idx()

  def create_widgets(self):
    self.menu = menu.UIMenu(self.root)
    self.input_label = Label(self.root, text="Pregunar:")
    self.box_text = StringVar()
    self.input_text = Entry(self.root, textvariable=self.box_text)
    self.ask_btn = Button(self.root, text="Consultar", command=self.answer_question) 
    self.output_text = scrolledtext.ScrolledText(self.root, wrap=WORD, width=70, height=20)

    self.input_label.grid(column=0, row=0, pady=5)
    self.input_text.grid(column=0, row=1, pady=5)
    self.ask_btn.grid(column=0, row=2, pady=5)
    self.output_text.grid(column=0, row=3, pady=10)

  def load_documents(self):
    conn_manager = manager.DAO().get_connect()
    conn = conn_manager['conn']
    cr = conn_manager['cr']
    cr.execute('SELECT id, title, content FROM documents')
    rows = cr.fetchall()
    conn.close()

    self.docs = []
    self.doc_texts = []

    for row in rows:
      doc = {
        "id": row[0],
        "titel": row[1],
        "text_content": row[2]
      }
      self.docs.append(doc)
      self.doc_texts.append(doc['text_content'])

  def build_idx(self):
    self.vectorize = TfidfVectorizer()
    self.doc_vectors = self.vectorize.fit_transform(self.doc_texts)

  def answer_question():
    pass

  def run(self):
    self.root.mainloop()

root = Root()
root.run()