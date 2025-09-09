try:
  import os
  import shutil
  from datetime import datetime
except ImportError as e:
  print('Error importing libraries ', e)

class BackupManager:
  def __init__(self, db_path, backup_folder='backups'):
    self.cwd = os.getcwd()
    self.db_path = db_path
    self.backup_folder = backup_folder
    # self.path_full = os.path.join(self.cwd, self.backup_folder)

    if not os.path.exists(self.backup_folder):
      os.makedirs(self.backup_folder)
      # os.makedirs(self.path_full)

  def create_backup(self):
    if not os.path.exists(self.db_path):
      print("No se encontró la base de datos para respaldar.")
      return False

    self.timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    self.backup_file = os.path.join(self.backup_folder, f'backup_{self.timestamp}.db')
    shutil.copy2(self.db_path, self.backup_file)
    print(f"Backup creado: {self.backup_file}")
    return True