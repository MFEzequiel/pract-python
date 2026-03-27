class CtrlDb:
  def __init__(self, model=None) -> None:
    self.model = model 

  def create_table(self):
    pass

  def add_product(self, data=[]) -> None:
    query_insert = 'INSERT INTO products (name, price, stock) VALUES (?,?,?)'
    self.model.executemany(query_insert, data)

  def delete_product(self, data=[]) -> None:
    query_insert = 'DELETE FROM products WHERE id=? OR name=? AND price=? AND stock=?'
    print(data)
    self.model.executemany(query_insert, data)