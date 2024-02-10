import sqlite3

connection = sqlite3.connect("tutorial.db")

cursor = connection.cursor()

#cursor.execute("CREATE TABLE movie(title, year, score)")

cursor.execute("""
               INSERT INTO movie VALUES
               ('Monty Python and the HOly Grail', 1975, 8.2),
               ('And Now for Something Completely Different', 1971, 7.5)
               """)

connection.commit()

for row in cursor.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)