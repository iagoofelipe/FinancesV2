from mysql.connector import connect

conn = connect(
    host='127.0.0.1',
    port=3306,
    username='test',
    password='1234',
    database='world'
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM country WHERE Continent='South America'")
print(cursor.fetchall())