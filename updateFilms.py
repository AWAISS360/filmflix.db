from connect2 import *

def update_film():
  idField = input("enter the filmID of the record to be updated: ")
  fieldName = input("enter Title, yearReleased, rating, duration or Genre as field name: ").title()
  fieldValue = input(f"enter the value for {fieldName} field: ")

  print(fieldValue)

  fieldValue = "'" + fieldValue + "'"
  print(fieldValue)


  dbCursor.execute(f"UPDATE tblfilms SET {fieldName} = {fieldValue} WHERE songID = {idField}")
  dbCon.commit()


  print(f"record {idField} updated in the songs table")

if __name__ == "__main__":
  update_film()
