try:
  import os
  import shutil
  from datetime import datetime
except ImportError as e:
  print('Error importing libraries:', e)

class BackupManager:
  def __init__(self, db_path, backup_folder='../backups'):
    self.db_path = db_path
    self.backup_folder = backup_folder

    if not os.path.exists(self.backup_folder):
      os.makedirs(self.backup_folder)

  def create_backup(self):
    if not os.path.exists(self.db_path):
      print("No se encontró la base de datos para respaldar.")
      return False

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = os.path.join(self.backup_folder, f'backup_{timestamp}.db')
    shutil.copy2(self.db_path, backup_file)
    print(f"Backup creado: {backup_file}")
    return True
