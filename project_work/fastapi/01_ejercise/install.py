import PyInstaller.__main__


PyInstaller.__main__.run([
  '--name=manager',      
  '--onefile',
  # '--windowed', # comentado para ver si se inicia el server
  '--add-data=server/app.py;.',      # copiar a la raíz del exe
  '--add-data=server/create_files.py;.',
  '--add-data=server/templates/assistence.html;.',
  '--add-data=server/templates;server/templates',
  '--add-data=server/templates/course.html;.',
  '--add-data=config.py;.',
  '--add-data=launcher.py;.',
  '--add-data=network.py;.',
  '--hidden-import=uvicorn',
  '--hidden-import=rich',
  '--hidden-import=server',
  '--hidden-import=openpyxl',
  '--hidden-import=pandas',
  '--specpath=.',         
  '--noconfirm',
  'launcher.py'
])