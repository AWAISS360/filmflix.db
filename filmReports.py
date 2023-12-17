from connect2 import *

# create subroutine 
def reports_menu():
  with open('reportoptions.txt') as reportOptions:
    userMenu = reportOptions.read()
  return userMenu


def film_reports():
  option1 = 0
  optionsList1 = ["1","2","3","4","5"]

  choiceMenu = reports_menu()

  while option1 not in optionsList1:
    print(choiceMenu)

    option1 = input("Enter an option from the FlimFlix Menu: ")

    if option1 not in optionsList1:
      print(f"{option1} is not a valid choice! ")
  return option1



def main_program1():
   mainProgram1 = True

   while mainProgram1:
     mainMenu1 = film_reports()

     if mainMenu1 == "1":

       dbCursor.execute("SELECT * FROM tblfilms")
       reports = dbCursor.fetchall()
       for aRecord in reports:
           print(aRecord)

     elif mainMenu1 == "2":

       genreChoice = str(input("What genre would you like to choose: ").title())
       dbCursor.execute(f"SELECT * FROM tblfilms WHERE Genre = '{genreChoice}' ")
       reports = dbCursor.fetchall()
       for aRecord in reports:
           print(aRecord)

     elif mainMenu1 == "3":

       yearChoice = int(input("What year would you like to choose from between '1920' and '2022': "))
       if yearChoice < 2022 and yearChoice > 1920:
         yearChoice = str(yearChoice)
         dbCursor.execute(f"SELECT * FROM tblfilms WHERE YearReleased = '{yearChoice}' ")
         reports = dbCursor.fetchall()
         for aRecord in reports:
             print(aRecord)
       else:
         print("Invalid Choice! ")

     elif mainMenu1 == "4":
       ratingOptions = ["NC-17", "PG", "G", "R", "PG-13"]
       print(ratingOptions)
       ratingChoice = input("What rating would you like to choose from the above: ").upper()
       if ratingChoice in ratingOptions:
         dbCursor.execute(f"SELECT * FROM tblfilms WHERE Rating = '{ratingChoice}' ")
         reports = dbCursor.fetchall()
         for aRecord in reports:
             print(aRecord)
       else:
         print("Invalid Choice! ")

     else:

       mainProgram1 = False

if __name__ == "__main__":
    film_reports()
    main_program1()
