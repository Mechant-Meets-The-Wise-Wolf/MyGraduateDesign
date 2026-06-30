import sqlite3,os


class SQLite(object):
    """SQLite 数据库操作类"""


    def __init__(self):
        """初始化，指定数据库文件路径"""
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.dbpath=os.path.join(self.current_dir,'Database.db')


    def connect(self):
        try:
            self.conn = sqlite3.connect(self.dbpath)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Error connecting to database:", e)

    def insert(self, table, fields):
        try:
            query = f"INSERT INTO {table} ({', '.join(fields.keys())}) VALUES ({', '.join(['?' for _ in range(len(fields))])})"
            self.cursor.execute(query, list(fields.values()))
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error inserting data:", e)

    def update(self, table, fields, condition=None):
        try:
            # Construct SET part of the query
            set_query = ', '.join([f"{key} = ?" for key in fields.keys()])
            
            # Construct WHERE part of the query
            where_query = ''
            values = list(fields.values())
            if condition:
                where_query = ' WHERE ' + ' AND '.join([f"{key} = ?" for key in condition.keys()])
                values.extend(condition.values())
            
            # Construct the complete query
            query = f"UPDATE {table} SET {set_query}{where_query}"
            
            # Execute the query
            self.cursor.execute(query, values)
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error updating data:", e)

    def delete(self, table, condition=None):
        try:
            query = f"DELETE FROM {table}"
            if condition:
                query += f" WHERE {condition}"
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error deleting data:", e)

    def select(self, table, fields=None, condition=None):
        try:
            # Construct the SELECT part of the query
            if fields:
                query = f"SELECT {', '.join(fields)} FROM {table}"
            else:
                query = f"SELECT * FROM {table}"
            
            # Construct the WHERE part of the query using the condition dictionary
            values = []
            if condition:
                conditions = [f"{key} = ?" for key in condition.keys()]
                query += f" WHERE {' AND '.join(conditions)}"
                values.extend(condition.values())

            # Execute the query
            self.cursor.execute(query, values)
            
            # Fetch and return the result
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print("Error selecting data:", e)
            return None
    #模糊查询
    def selectlike(self, table, fields=None, like_str=None):
        sql = f"SELECT * FROM {table} WHERE {fields} like '%{like_str}%'"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows
    
    def userlogin(self, username, password):
            query = f"SELECT * FROM usertable WHERE account_name ='{username}' AND pass_word = '{password}'"
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result
  
    def usercheck(self, username):
            query = f"SELECT * FROM usertable WHERE account_name ='{username}'"
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result

    def selectmax(self, table, field):
            
            query = f"SELECT MAX({field}) FROM {table}"
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result
    
    def close(self):
            self.conn.close()

