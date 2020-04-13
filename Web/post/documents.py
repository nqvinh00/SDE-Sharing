import os
import mysql.connector

def updateDocuments():
	db = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "root",
		database = "web"
		)
	mycursor = db.cursor(buffered=True)
	directory = "D:/Python/Project1/Source/Documents"
	for (path, dirnames, filenames) in os.walk(directory):
		for i in filenames:
			source = path + "/" + i
			name = i[0:len(i) - 4]
			value = (name, source)
			print(value)
			mycursor.execute('SELECT * FROM post_documents')
			row = mycursor.fetchall()
			source_check = [i[2] for i in row]
			if source not in source_check:
				mycursor.execute('INSERT INTO post_documents (name, source) VALUES (%s, %s)', value)
	db.commit()