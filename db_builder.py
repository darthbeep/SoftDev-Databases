import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

#I just switched from platformio terminal to ult terminal in atom and my workspace so much prettier 10/10
#That said, I really need to invest in a smoother way to delete files
with open('csv/courses.csv') as csvfile:
	courses = csv.DictReader(csvfile)
	command = "CREATE TABLE courses (" + courses.fieldnames[0] + " TEXT, " + courses.fieldnames[1] + " INT, " + courses.fieldnames[2] + ");" #I wanted to make it work for any csv but got lazy half way through, so it can only work for text, int, int csvs
	c.execute(command)
	for row in courses:
		command = "INSERT INTO courses VALUES (\'" + row[courses.fieldnames[0]] + "\', " + row[courses.fieldnames[1]] + ", " + row[courses.fieldnames[2]] + ");"
		c.execute(command);
	#c.execute("SELECT * FROM courses;")
	#print c.fetchall()

with open('csv/peeps.csv') as csvfile: #Wow it's almost like this is just a copy/paste of the last one
	peeps = csv.DictReader(csvfile)
	command = "CREATE TABLE peeps (" + peeps.fieldnames[0] + " TEXT, " + peeps.fieldnames[1] + " INT, " + peeps.fieldnames[2] + ");"
	c.execute(command)
	for row in peeps:
		command = "INSERT INTO peeps VALUES (\'" + row[peeps.fieldnames[0]] + "\', " + row[peeps.fieldnames[1]] + ", " + row[peeps.fieldnames[2]] + ");"
		c.execute(command);
	#c.execute("SELECT * FROM peeps;")
	#print c.fetchall()


#command = ""          #put SQL statement in this string
#c.execute(command)    #run SQL statement

#==========================================================
db.commit() #save changes
db.close()  #close database
