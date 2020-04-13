import os
import mysql.connector

def updateExams():
	db = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "root",
		database = "web"
		)
	mycursor = db.cursor(buffered=True)
	directory = "D:/Python/Project1/Source/Examination"
	for (path, dirnames, filenames) in os.walk(directory):
		for i in filenames:
			print(i)
			source = path + "/" + i
			exam_id, name, teacher = i.split('-')
			teacher = teacher[0:len(teacher) - 4]
			value = (exam_id, name, teacher, source)
			mycursor.execute('SELECT * FROM post_exams')
			row = mycursor.fetchall()
			source_check = [i[4] for i in row]
			if source not in source_check:
				mycursor.execute('INSERT INTO post_exams (exam_id, name, teacher, source) VALUES (%s, %s, %s, %s)', value)
	db.commit()
