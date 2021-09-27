import sqlite3
import pandas as pd

# Create connection and cursor to demo database
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# Create demo table
create_table = "CREATE TABLE IF NOT EXISTS demo (s TEXT NOT NULL, x INTEGER NOT NULL , y INTEGER NOT NULL )"
curs.execute(create_table)

# Insert data into demo table
insert = "INSERT INTO demo VALUES (?, ?, ?)"
records = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]
curs.executemany(insert, records)
conn.commit()


# Create queries
row_count = "SELECT COUNT(*) FROM demo"
xy_at_least_5 = "SELECT COUNT(*) FROM demo WHERE x = 5 AND y = 5"
unique_y = "SELECT COUNT (DISTINCT y) FROM demo"


# Execute queries
q1 = curs.execute(row_count).fetchall()
q2 = curs.execute(xy_at_least_5).fetchall()
q3 = curs.execute(unique_y).fetchall()

print(pd.DataFrame(q1))
print(pd.DataFrame(q2))
print(pd.DataFrame(q3))
