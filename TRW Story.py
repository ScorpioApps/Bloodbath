import sys, random

############################################################
################## WELCOME + CLASS CHOICES #################
############################################################

def startUp ():
  print ("--------------------\n----- BLOODBATH ----\n--------------------")
  print ("Choose your character:")
  print ("- Apprentice: A young, energetic apprentice on a quest to be a Mage, guided by his wise teacher.")
  print ("- Assassin: An assassin-in-training, taught by a retired soldier to hunt down the countries worst threats.")
  print ("- Warlord: A warrior being taught by a leader in the Bloodbath War.")
  classChoose ()

def classChoose ():
  global charClass
  userInp = input ("> ")
  if userInp == "Apprentice":
    charClass = "Apprentice"
    gameStory ()
  elif userInp == "Assassin":
    charClass = "Assassin"
    gameStory ()
  elif userInp == "Warlord":
    charClass = "Warlord"
    gameStory ()
    
def gameStory ():
  if charClass == "Apprentice":
    print ("Mage: Why, hello there!")
    print ("Mage: I am the Master Mage, and you must be my new apprentice!")
  
