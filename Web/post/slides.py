import os
import mysql.connector

db = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "root",
	database = "web"
	)
mycursor = db.cursor(buffered=True)
directory = "D:/Python/Project1/Source/Slides"
y = [x[0] for x in os.walk(directory) if x[0] != directory]
for x in y:
	slide_id, name, teacher = x[len(directory) + 1: len(x)].split('-')
	value = (slide_id, name, teacher, x)
	mycursor.execute('SELECT * FROM post_slides')
	row = mycursor.fetchall()
	source_check = [i[4] for i in row]
	if x not in source_check:
		mycursor.execute('INSERT INTO post_slides (slide_id, name, teacher, source) VALUES (%s, %s, %s, %s)', value)
db.commit()
