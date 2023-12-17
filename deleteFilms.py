from connect2 import *
# create subroutine 
def delete_films():    
  # use primary key to delete a record     
  idField = input("Enter the filmID of the record to be deleted: ")    
  # DELETE FROM songs WHERE SongID = 1/2/3/4/5/.....    
  dbCursor.execute(f"DELETE FROM tblfilms WHERE FilmID = {idField}")    
  dbCon.commit()    
  print(f"Record {idField} deleted from tblfilms table ")
  
if __name__ == "__main__":    
  delete_films()