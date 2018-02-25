import sys, random

############################################################
################## WELCOME + CLASS CHOICES #################
############################################################

def startUp ():
  print ("--------------------\n----- BLOODBATH ----\n--------------------")
  print ("Choose your character:")
  print ("- Mage's Apprentice: A young, energetic apprentice on a quest to be a Mage, guided by his wise teacher.")
  print ("- Assassin: An assassin-in-training, taught by a retired soldier to hunt down the countries worst threats.")
  print ("- Warlord: A warrior being taught by a leader in the Bloodbath War.")
  classChoose ()

def classChoose ():
  global charClass
  userInp = input ("> ")
  if userInp == "Mage's Apprentice":
    charClass = "Mage's Apprentice"
    gameStory ()
  elif userInp == "Assassin":
    charClass = "Assassin"
    gameStory ()
  elif userInp == "Warlord":
    charClass = "Warlord"
    gameStory ()
    
def gameStory ():
  if charClass == "Mage's Apprentice":
  
