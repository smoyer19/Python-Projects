

#Using the provided file list as list of strings variable
fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#importing sqlite to use with Python database creation
import sqlite3

#using a variable with connect function to call my database
conn = sqlite3.connect('Assignment.db')

#adding cursor to make changes to database
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('Assignment.db')
#using ends with to iterate through fileList for .txt files and toinsert filelist variable with only txt files into database
with conn:
    cur = conn.cursor()
    for file in fileList:
        if file.endswith(".txt"):
            cur.execute ("INSERT INTO tbl_files(col_fileName) VALUES (?)", (file,))
    conn.commit
conn.close()

conn = sqlite3.connect('Assignment.db')

with conn:
    cur = conn.cursor()
    # executes a SELECT statement to grab the contents of the table
    cur.execute("SELECT * FROM tbl_files")
    # saves the info from the SELECT statement to a variable named "results"
    results = cur.fetchall()
    # prints the "results" variable
    print(results)
conn.close()
