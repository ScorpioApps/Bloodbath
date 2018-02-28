import sys, random, time

############################################################
################## WELCOME + CLASS CHOICES #################
############################################################

def startUp ():
  print ("--------------------\n----- BLOODBATH ----\n--------------------")
  print ("Choose your character:")
  print ("- Apprentice: A young, energetic apprentice on a quest to be a Mage, guided by his wise teacher.")
  print ("- Assassin: An assassin-in-training, taught by a retired soldier to hunt down the country's worst threats.")
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
    print ("Why, hello there!")
    time.sleep (2.43)
    print ("I am the Master Mage, and you must be my new apprentice!")
    time.sleep (4)
    print ("Well, let's get right to it! I'll teach you your first spell!")
    time.sleep (4.3)
    print ("I think we should try Earthquake!")
    time.sleep (3.5)
    print ("No? Maybe not, you might break a few things.")
    time.sleep (3.83)
    print ("How about Fireball?")
    time.sleep (4)
    print ("I knew you'd like that!")
    time.sleep (2)
    print ("Just wave your hands around, in a mystical way, and shout 'ALAKAZAM!'")
    time.sleep (4.4)
    print ("No, the hand thing doesn't do anything. You'll just look more Mage-like.\nAnd I also just wanted to see you look like an idiot.")
    time.sleep (5)
    print ("Anyway, go on. Say 'Alakazam'!")
    firstSpell ()
    
def firstSpell ():
  inp = input ("> ")
  if inp == "Alakazam":
    gameStory2 ()
  else:
    print ("Write properly, please!")
    return firstSpell ()

startUp ()
    
