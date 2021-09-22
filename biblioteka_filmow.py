import random
class Film:
    def __init__(self, title, the_year_of_publishment, type, number_of_plays,):
        self.title = title
        self.the_year_of_publishment = the_year_of_publishment
        self.type = type
        self.number_of_plays = number_of_plays
    
    def play(self):
        for a in lista:
         number_of_plays = a.number_of_plays + 1
         print(number_of_plays)

    def film(self): 
         self.title = input("Nazwa filmu:")
         for a in lista:
            if self.title == a.title:
             return(f"{self.title}({self.the_year_of_publishment})")     

class Series(Film):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number
    
    def serie(self):
        self.title = input("Nazwa serialu:")
        for a in lista:
           if self.title == a.title:
            return(f"{self.title} S{self.season_number}E{self.episode_number}")

lista = [] 
lista.append(Series(title = "Narcos", the_year_of_publishment = "2015", type = "Crime TV genre", number_of_plays = 15000000, episode_number = "07", season_number = "01"))
lista.append(Film(title = "Creed", the_year_of_publishment = "2015", type = "Sport film", number_of_plays = 71323581))
lista.append(Series(title = "Punisher", the_year_of_publishment = "2017", type = "Conspiracy fiction", number_of_plays = 4214125, episode_number = "02", season_number = "04"))
lista.append(Film(title = "Sniper", the_year_of_publishment = "2014", type = "Action", number_of_plays = 9124531))


rodzaj = input("Film czy Serial:")
for a in lista: 
    if rodzaj =="serial" and type(a)== Series:
      print(a.serie())
      break
    elif rodzaj == "film" and type(a)== Film:
      print(a.film())
      break

seriale = input("Czy chcesz zwrócić liste wszytkich seriali? Tak/Nie  ")    
def get_series():
    for a in lista:
        if seriale == "Tak":
            if type(a)== Series:
             print((a.title))
        if seriale == "Nie":
            break
get_series()

filmy = input("Czy chcesz zwrócić liste wszytkich filmów? Tak/Nie  ")    
def get_films():
    for a in lista:
        if filmy == "Tak":
            if type(a)== Film:
             print((a.title))
        if filmy == "Nie":
            break
get_films()

search = input("Szukaj filmu/serialu po nazwie: ")
def szukaj():
    for a in lista:
        if search == a.title:
            print(f"{a.title}, {a.the_year_of_publishment}, {a.type}, {a.number_of_plays}")
        if search != a.title:
            break
szukaj()      

losowe = input("Czy chcesz wylosować film/serial? Tak/Nie  ")
def generate_views():
      if losowe == "Tak":
          print (random.choice(lista).title)
          print("number of plays:", random.choice(range(1000000, 100000000)))
      
          
generate_views()

dycha = input("Czy chcesz wylosować 10 razy? Tak/Nie ")
def dyszka():
    if dycha == "Tak":
        for i in range(10):
         generate_views()
dyszka()
 

popular = input("Napisz Tak/Nie, jeśli chcesz zobaczyć najpopularniejsze tytuły:  ") 
def top_titles():
    def myFunc(e):
      return e.number_of_plays
    if popular == "Tak":
     lista.sort(reverse = True, key = myFunc)
     for a in lista:
         print(a.title)

top_titles()
        



