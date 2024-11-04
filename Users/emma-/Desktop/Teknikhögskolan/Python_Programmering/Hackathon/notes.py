#kategorier för quiz:

#Terminal:
#ls - se mappar och filer där du befinner dig
#ls - la - se gömda filer
#cd - plus mappnamn för att gå in i mappen eller gå tillbaka
#touch - för att skapa en fil
#python3 + filnamn (MAC)
#pwd - print the current working directory
#mkdir - skapa ny mapp
#rmdir - remove a mapp
#nano + filnamn = kommer till text editor#mv - byt namn och flytta 
#ctrl x + y = för att ta sig ut nano

#Git





#Klasser / Objektorienterad Programmering
# objektattribut - definiera ett attribut och accessa attributen
# class - (ritningen för våra objekt)
# instance / object - (det vi SKAPAR utifrån en class)
# instantiate (att skapa ett objekt), tex. student_1 = Student() --> vi instantierar
# instance variables / data attributes (variabler inne i våra objet/instanser)
# attributes (metoder + variabler)
# class variabel - tilldelade i class default ( förbestämd )
# method (funktioner inne i class)
# __init__ (constructor method, methods med dubbla understräck kallas för dunder methods)
# self (vårt handtag för att jobba med andra saker inom objektet)
# encapsulation - idén om att vi parar ihop data med variabler, och dessa inte ska "röra" världen / scopet som finns utanaför objekten. Också idén om att det globala scopet ska undvika att interagera med protected methods & variables.
# protected variables, prefixas med _ och betyder att dessa variabler får endast användas INNE i din klass genom .self
# protected methods, prefixas med _ och betyder att dessa variabler får endast användas INNE i din klass genom .self

# inheritance - idén om att klasser kan ärva instance variables och methods från en eller flera andra klasser
# base class / super class / parent class : SAMMA ORD, klassen som vi INHERITAR FRÅN
# child class, subclass : SAMMA ORD, klassen som ska INHERITA FRÅN en parent-klass 
# .super().__init__() - Vi anropar init-metoden på vår superklass och ser till att vi för vidare data från child-classens init-metod till parent-klassens init-metod

# abstraction - idén om att klasser är bra för att skapa komplex logik, men att en användare enkelt kan utnyttja den logiken genom att bara anropa metoder. personen behöver inte bry sig om implementationen, den behöver bara förstå hur den ska använda den! 




#Quiz
#Varför behöver vi flödes kontroll när vi programmerar?
#-för att fatta beslut baserat på villkor 
#-repetetera uppgifter effektivt
#-hantera fel
#-vara dynamisk och flexibla
#-förbättra effektiviteten och läsbarheten

#Vad är skillnaden på en for och while loop? När ska man använda vad?
#-En for loop används när vi vet hur många gånger vi ska iterera och while loop när vi inte vet.

#Vad kallas ett block av kod som utför en specifik sak? -
#-Funktion 

#Vad kallas variablerna vi skriver in vid skapandet av funktionen och vad kallas värdet vi skickar med när vi kallar på funktionen?
#-Parameter 
#-Argument 

#Vilka parameter typer finns det i funktioner? 
#- default 
#- positionell parameter (skriver ut t.ex. name = "Emma")

# Hur skriver man ut en dictionary och en lista? 
# - Dictionary = {}, Lista = []

#Vad skiljer sig en lista och en dictionary? 
#- En lista loopar vi igenom tills vi hittar det vi söker
#- En dictionary har en nyckel och ett unikt värde som tar oss direkt dit vi söker

#Vilka olika typer finns inom error handling? 
#LBYL
#EAFP

#Vilken tillhör: try, except, else, finally  - lbyl or EAFP

#Vilka typer av errors i Python kan man få? Nämn några exceptions man kan raisa
#-ZeroDivisionError
#-ValueError
#-TypeError

#Syntax error sker när koden omvandlas till bytecode
#medan det som inte är syntax error sker under runtime  -exceptions

#with open json - "r" och "w" - vad skiljer dom sig åt



#Virtual Enviroments & Externa packages
#Vad är PIP? 
#-pip är en package manager

#Venv
#-Hur skapar man en i terminalen? 
#-Hur aktiverar man den?

#Pip freeze
#-skapar filen requirments.txt och sparar alla paket vi har kopplade till projektet

#pip install -r requirements.txt 
# - installerara alla paket från en requriements.txt

#Vad är API
#- 
