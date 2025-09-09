try:
  import os
  import pandas as pd
  from core.file_manager import FileManager
except ImportError as e:
  print('Error importing libraries ', e)


def test_export_to_excel(tmp_path):
    data = [(1, "Carlos", "pass123")]
    file = tmp_path / "test_export.xlsx"
    
    # Export manually
    df = pd.DataFrame(data, columns=["ID", "Nombre", "Contraseña"])
    df.to_excel(file, index=False)

    # Now verify the file exists and is readable
    assert file.exists()

    df_read = pd.read_excel(file)
    assert df_read.loc[0, "Nombre"] == "Carlos"
