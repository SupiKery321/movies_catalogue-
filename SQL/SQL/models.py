import sqlite3


class TodosSQLite:
    def __init__(self, db_file):
          self.conn = self.create_connection(db_file=db_file)
    
    def create_connection(self, db_file):
       """ create a database connection to the SQLite database
           specified by db_file
       :param db_file: database file
       :return: Connection object or None
       """
       conn = None
       try:
         conn = sqlite3.connect(db_file)
         return conn
       except sqlite3.Error as e:
           print(e)
       return conn
    
    def create(self, sql):
       """
       Create a new projekt into the projects table
       :param conn:
       :param projekt:
       :return: projekt id
       """
       cur = self.conn.cursor()
       cur.execute(sql)
       self.conn.commit()
       return cur.lastrowid
    
    def get(self, id):
        sql = [sql for sql in self.all() if sql['id'] == id]
        if sql:
         return sql[0]
        return []
    
    def select_all(self, table):
       """
       Query all rows in the table
       :param conn: the Connection object
       :return:
       """
       cur = self.conn.cursor()
       cur.execute(f"SELECT * FROM {table}")
       rows = cur.fetchall()

       return rows
    def select_where(self, table, **query):
       """
       Query tasks from table with data from **query dict
       :param conn: the Connection object
       :param table: table name
       :param query: dict of attributes and values
       :return:
       """
       cur = self.conn.cursor()
       qs = []
       values = ()
       for k, v in query.items():
           qs.append(f"{k}=?")
           values += (v,)
       q = " AND ".join(qs)
       cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
       rows = cur.fetchall()
       return rows
    
    
    def update(self, table, id, **kwargs):
       """
       update status, begin_date, and end date of a task
       :param conn:
       :param table: table name
       :param id: row id
       :return:
       """
       parameters = [f"{k} = ?" for k in kwargs]
       parameters = ", ".join(parameters)
       values = tuple(v for v in kwargs.values())
       values += (id, )

       sql = f''' UPDATE {table}
                 SET {parameters}
                 WHERE id = ?'''
       try:
           cur = self.conn.cursor()
           cur.execute(sql, values)
           self.conn.commit()
           print("OK")
       except sqlite3.OperationalError as e:
           print(e)

    if __name__ == "__main__":
       conn = create_connection("database.db")
       update(conn, "tasks", 2, status="started")
       update(conn, "tasks", 2, stat="started")
       conn.close()

SQL = TodosSQLite(db_file="database.db")
