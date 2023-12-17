from connect2 import *

def read_films():
  dbCursor.execute("SELECT * FROM tblfilms")

  allRecords = dbCursor.fetchall()

  for eachRecord in allRecords:
    print(eachRecord)

if __name__ == "__main__":
  read_films()