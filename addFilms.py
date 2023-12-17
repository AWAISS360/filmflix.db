from connect2 import *

def insert_film():
  filmTitle = str(input("enter film title: ").title())
  filmYear = int(input("enter film release year: "))
  filmRating = str(input("enter film rating: "))
  filmDuration = int(input("enter film duration: "))
  filmGenre = str(input("enter film genre: "))


  dbCursor.execute("INSERT INTO tblfilms(title, yearReleased, rating, duration, genre) VALUES(?,?,?,?,?)", (filmTitle, filmYear, filmRating, filmDuration, filmGenre))

  dbCon.commit()
  
  print(f"{filmTitle} inserted in the Film table")

if __name__ == "__main__":
  insert_film()