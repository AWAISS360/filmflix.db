import addFilms, deleteFilms, updateFilms, readFilms, filmReports

def menu_file():
  with open('menuoptions.txt') as filmsFile:
    userMenu = filmsFile.read()
  return userMenu


def films_menu():
  option = 0
  optionsList = ["1","2","3","4","5"]

  choiceMenu = menu_file()

  while option not in optionsList:
    print(choiceMenu)

    option = input("Enter an option from the FlimFlix Menu: ")

    if option not in optionsList:
      print(f"{option} is not a valid choice! ")
  return option

mainProgram = True

while mainProgram:
  mainMenu = films_menu()

  if mainMenu == "1":
    addFilms.insert_film()
  elif mainMenu == "2":
    deleteFilms.delete_films()
  elif mainMenu == "3":
    updateFilms.update_film()
  elif mainMenu == "4":
    readFilms.read_films()
  elif mainMenu == "5":
    filmReports.film_reports()
    filmReports.main_program1()
  else:
    mainProgram = False
input("Enter to quit the FilmFlix App")
