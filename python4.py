DELETE = 'd'
EXTENSIE = '.wrd'
KIES_LIJST = 'k'
MAX_WOORDLENGTE = 20
NIEUWE_LIJST = 'n'
OPSLAAN = 'w'
OVERHOREN = 'o'
SCHEIDER = '='
SCHERMBREEDTE = 80
SCHERMHOOGTE = 40
STANDAARD_LIJST = 'EN-NED'
STOPPEN = 'q'
TOEVOEGEN = 't'
doorgaan = True

import os

def leeg_scherm():
    os.system("clear")

def kies_lijst():
    return input("Kies een lijst: ")


def lees_woordenlijst(bestandsnaam):
    woordenlijst = {}
   
    with open(bestandsnaam) as f:
      for r in f:  
         key, value = r.strip().split(SCHEIDER)
         woordenlijst[key] = value
    
    return woordenlijst

def main():
    huidige_lijst_naam = STANDAARD_LIJST
    woordenlijst = lees_woordenlijst(huidige_lijst_naam + EXTENSIE)
    print_menu(huidige_lijst_naam)
    while (keuze := input("Kies: ")) != "5":
       if keuze == "1":
          nieuwe_lijst = nieuwe_lijst_naam()
          huidige_lijst_naam = nieuwe_lijst
          woordenlijst = {}
          schrijf_woordenlijst(huidige_lijst_naam + EXTENSIE, woordenlijst)
       elif keuze == "2":
          huidige_lijst_naam = kies_lijst()
          woordenlijst = lees_woordenlijst(huidige_lijst_naam + EXTENSIE)
       elif keuze == "3":
          voeg_woorden_toe(woordenlijst, huidige_lijst_naam)
       elif keuze == "4":
          overhoren(woordenlijst)
       else:
          print("Keuze bestaat niet, probeer opnieuw: ")
      
       print_menu(huidige_lijst_naam)
      
    print_afscheid()

def nieuwe_lijst_naam():
   return input("Geef de woordenlijst een naam: ")

import random

def overhoren(woordenlijst):
   vertaling = random.choice(list(woordenlijst))
   woord = woordenlijst[vertaling]
   while (antwoord := input(f"Wat is de vertaling van '{woord}'? (q om te stoppen):")) != STOPPEN:
      if antwoord == vertaling:
          print("Goed!")
          vertaling = random.choice(list(woordenlijst))
          woord = woordenlijst[vertaling]
      else:
         print(f"Fout! De antwoord is '{vertaling}'.")
        
def print_afscheid():
    leeg_scherm()
    print_header()
    print_regel(" Bedankt voor het gebruiken van het overhoorprogramma!")
    print_footer()

def print_footer():
    print("|" + " " * (SCHERMBREEDTE - 2) + "|")
    print("=" * SCHERMBREEDTE)

def print_header():
   print("=" * SCHERMBREEDTE)
   print("|" + " " * (SCHERMBREEDTE - 2) + "|")

   
def print_menu(lijst_naam):
    leeg_scherm()
    print_header()
    print_regel(f" Geselecteerde lijst: {lijst_naam}")
    print_regel('')
    print_regel(" Menu:")
    print_regel(" 1 = Nieuwe woordenlijst maken")
    print_regel(" 2 = Veranderen van woordenlijst")
    print_regel(" 3 = Woorden toevoegen aan een woordenlijst")
    print_regel(" 4 = Woordenlijsten overhoren")
    print_regel(" 5 = Stoppen met het programma")
    print_footer()


def print_regel(inhoud=''):
    print(f"| {inhoud.ljust(SCHERMBREEDTE - 4)} |")

def schrijf_woordenlijst(bestandsnaam, woordenlijst):
    with open(bestandsnaam, 'w') as f:
        for key, value in woordenlijst.items():
            f.write(f"{key}{SCHEIDER}{value}\n")

def verwijder_woord(woord, woordenlijst):
   zeker = input(f"Weet je zeker dat je '{woord}' wilt verwijderen? (ja/nee): ")
   if zeker == "ja":
        woordenlijst.pop(woord, None)
        print(f"'{woord}' is verwijderd.")
   else:
        print(f"'{woord}' is niet verwijderd.")

def voeg_woorden_toe(woordenlijst, lijst_naam):
   while (woord := input(f"Wat is de vertaling van '{woord}'? (q om te stoppen):")) != STOPPEN :
        vertaling = input(f"Wat is de vertaling van '{woord}'? ")
        woordenlijst[woord] = vertaling
        schrijf_woordenlijst(lijst_naam + EXTENSIE, woordenlijst)


main()   