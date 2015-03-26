import sqlite3
conn = sqlite3.connect(db_file)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute(sql, [unix_time])
return cursor.fetchall()
