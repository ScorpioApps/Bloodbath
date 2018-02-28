import sys, random

############################################################
################## WELCOME + CLASS CHOICES #################
############################################################

def startUp ():
  print ("Welcome to Bloodbath.")
  print ("Bloodbath is an RPG turn-based game.")
  info1 ()

def info1 ():
  print ("You can be any of these three classes.")
  print ("- Mage\n- Assassin\n- Warlord")
  print ("Type a name to find out more.")
  classInfo ()

def classInfo ():
  class_info = input ("> ")
  if class_info == "Mage":
    mageInfo ()
  elif class_info == "Assassin":
    assassinInfo ()
  elif class_info == "Warlord":
    warlordInfo ()
  else:
    print ("Sorry, that's an invalid choice. All inputs are case-sensitive. Please type your response again.")
    return classInfo ()
    
def mageInfo ():
  print ("The Mage is a mystical character with four unique powers:") ## Info for the Mage class
  print ("1. Fireball - 6 DMG, 60% ACC\n2. Water Jet - 4 DMG, 60% ACC\n3. Earthquake - 9 DMG, 40% ACC\n4. Thorny Whip - 4 DMG, 75% ACC") ## Mage's powers
  print ("Stats:\nHealth: 15\nStrength: 7\nDexterity: 11") ## Mage's stats
  print ("Would you like to be this character?")
  charChoiceMage () ## Asking user if this will be their character

def assassinInfo ():
  print ("The Assassin has trained for years, gaining incredible dexterity and strength. He relies on his array of weapons to use as his four powers:") ## Info for the Assassin class
  print ("1. Knife Plunge - 8 DMG, 70% ACC\n2. Bullets - 12 DMG, 60% ACC\n3. Hand-to-hand - 9 DMG 75% ACC\n4. Precise Snipe - 15 DMG, 80% ACC") ## Assassin's powers
  print ("Stats:\nHealth: 30\nStrength: 12\nDexterity: 17") ## Assassin's stats
  print ("Would you like to be this character?")
  charChoiceAssassin ()

def warlordInfo ():
  print ("The Warlord is a mighty warrior, with ample strength. His fists and trusty hammer are the only weapons he needs for his four powers:") ## Info for the Warlord class
  print ("1. Hammer Smash - 13 PWR\n2. Rapid Punches - 10 PWR\n3. Big Kick - 7 PWR\n4. Headbutt - 5 PWR") ## Warlord's powers
  print ("Stats'\nHealth: 50\nStrength: 18\nDexterity: 7") ## Warlord's stats
  print ("Would you like to be this character?")
  charChoiceWarlord ()
  
def charChoiceMage ():
  charChoice = input ("> ")
  if charChoice == "yes":
    mageGame ()
  elif charChoice == "no":
    print ("Would you like to quit the game?")
    wantQuit ()
  else:
    print ("You know Computer Programmers have lives? You know, the people putting effort into making you guys awesome games? We don't have the time to write code for people who can't type 'yes' or 'no'. Seriously. Just answer properly.")
    return charChoiceMage ()

def charChoiceAssassin ():
  charChoice = input ("> ")
  if charChoice == "yes":
    assassinGame ()
  elif charChoice == "no":
    print ("Would you like to quit the game?")
    wantQuit ()
  else:
    print ("You know Computer Programmers have lives? You know, the people putting effort into making you guys awesome games? We don't have the time to write code for people who can't type 'yes' or 'no'. Seriously. Just answer properly.")
    return charChoiceAssassin ()

def charChoiceWarlord ():
  charChoice = input ("> ")
  if charChoice == "yes":
    warlordGame ()
  elif charChoice == "no":
    print ("Would you like to quit the game?")
    wantQuit ()
  else:
    print ("You know Computer Programmers have lives? You know, the people putting effort into making you guys awesome games? We don't have the time to write code for people who can't type 'yes' or 'no'. Seriously. Just answer properly.")
    return charChoiceWarlord ()
  
############################################################
######################## MAGE GAME #########################
############################################################

def mageGame ():
  print ("You are a Mage!")
  print ("Get ready for your first battle! I'll walk you through it.")
  print ("Your first enemy is a Skeleton. An easy first enemy.")
  print ("In a battle, you have three options:\n1. Attack\n2. Block\n3. Retreat")
  print ("When you attack, you can use the four moves mentioned earlier.\nBlocking will block the next attack the enemy makes, but you only have a limited number of moves to defeat the enemy, so don't overuse it.\nOnly retreat when necessary. You won't die, but you won't win the battle either.")
  print ("Now it's time for your first move!")
  global heroHealth, enemyHealth
  heroHealth, enemyHealth = 15, 10
  return mageLoop1 ()
 
############################################################
###################### MAGE BATTLE 1 #######################
############################################################
  
def mageLoop1 ():
  count = 1
  for count in range(7):
    print ("--------------------\n--------------------\nYour turn!")
    print ("What do you want to do?\n- Attack\n- Block\n- Retreat")
    mageMoveChoice1 ()
    if enemyHealth <= 0:
      return mageBattle1Win ()
    mageEnemyAttack1 ()
    if heroHealth <= 0:
      return mageBattle1Lose ()
    count += 1
    if count == 6:
      return mageBattle1Tired ()
    else:
      continue
    
def mageMoveChoice1 ():
  moveChoiceInp = input ("> ")
  if moveChoiceInp == "Attack":
    return mageAttackChoice1 ()
  elif moveChoiceInp == "Block":
    return mageBlock1 ()
  elif moveChoiceInp == "Retreat":
    return mageRetreat1 ()
  else:
    print ("You can Attack, Block and Retreat. Choose one of these options.")
    return mageMoveChoice1 ()
    
def mageAttackChoice1 ():
  print ("1. Fireball\n2. Water Jet\n3. Earthquake\n4. Thorny Whip")
  print ("What attack do you want to use? Type 'Back' if you want to do something else.")
  attackChoiceInp = input ("> ")
  if attackChoiceInp == "Fireball":
    return mageFireball1 ()
  elif attackChoiceInp == "Water Jet":
    return mageWaterJet1 ()
  elif attackChoiceInp == "Earthquake":
    return mageEarthquake1 ()
  elif attackChoiceInp == "Thorny Whip":
    return mageThornyWhip1 ()
  elif attackChoiceInp == "Back":
    print ("Going back...")
    return mageMoveChoice1
  else:
    print ("That's an invalid choice. All inputs are case-sensitive. Please try again.")
    return mageAttackChoice1 ()
    
def mageFireball1 ():
  global enemyHealth
  attackHit = random.randint (1,5)
  if attackHit <= 3:
    print ("Skeleton has",enemyHealth,"Health!\nMage throws Fireball!\nSkeleton takes 6 DMG!\nSkeleton has",enemyHealth - 6,"Health!")
    enemyHealth -= 6
  else:
    print ("Skeleton has",enemyHealth,"Health!\nMage throws Fireball!\nFireball misses!\nSkeleton still has",enemyHealth,"Health!")

def mageWaterJet1 ():
  global enemyHealth
  attackHit = random.randint(1,7)
  if attackHit <= 4:
    print ("Skeleton has",enemyHealth,"Health!\nMage uses Water Jet!\nSkeleton takes 4 DMG!\nSkeleton has",enemyHealth - 4,"Health.")
    enemyHealth -= 4 
  else:
    print ("Skeleton has",enemyHealth,"Health!\nMage uses Water Jet!\nWater Jet misses!\nSkeleton still has",enemyHealth,"Health!")

def mageEarthquake1 ():
  global enemyHealth
  attackHit = random.randint (1,8)
  if attackHit <= 3:
    print ("Skeleton has",enemyHealth,"Health!\nMage creates an Earthquake!\nSkeleton takes 9 DMG!\nSkeleton has",enemyHealth - 9,"Health.")
  else:
    print ("Skeleton has",enemyHealth,"Health!\nMage creates an Earthquake!\nEarthquake misses!\nSkeleton still has",enemyHealth,"Health!")

def mageThornyWhip1 ():
  global enemyHealth
  attackHit = random.randint(1,4)
  if attackHit <= 3:
    print ("Skeleton has",enemyHealth,"Health!\nMage uses Thorny Whip!\nSkeleton takes 4 DMG!\nSkeleton has",enemyHealth - 4,"Health.")
    enemyHealth -= 4 
  else:
    print ("Skeleton has",enemyHealth,"Health!\nMage uses Thorny Whip!\nThorny Whip misses!\nSkeleton still has",enemyHealth,"Health!")
  
def mageEnemyAttack1 ():
  global heroHealth
  attackHit = random.randint (1,25)
  print ("--------------------\n--------------------\nEnemy's turn!")
  if attackHit <= 5:
    print ("Mage has",heroHealth,"Health!\nSkeleton throws his Spare Femur!\nSpare Femur Throw misses!\nMage still has",heroHealth,"Health!")
  elif attackHit > 5 <= 15:
    print ("Mage has",heroHealth,"Health!\nMage gets hit by False Teeth!\nMage takes 4 DMG!\nMage has",heroHealth - 4,"Health.")
    heroHealth -= 4
  elif attackHit > 15 <= 25:
    print ("Mage has",heroHealth,"Health!\nMage gets hit by Phalanx Stab!\nMage takes 6 DMG!\nMage has",heroHealth - 6,"Health.")
    heroHealth -= 6
  else:
    print ("error in code :/") 
    
def mageBlock1 ():
  print ("Mage uses Block! Mage blocks Enemy's next attack!")
  print ("It's Mage's turn again!")
  return mageMoveChoice1 ()
  
def mageBattle1Win ():
  print ("Well done, Mage! You won your first Battle! Get ready, you're about to start Battle 2!")
  return mageBattle2 ()
  
def mageBattle1Lose ():
  print ("Oh no, Mage! You lost! Don't worry, you'll win the next Battle!")
  return mageBattle2 ()

def mageBattle1Tired ():
  print ("Mage got tired of fighting! Mage lost!\nDon't worry you'll win the next Battle. Just remember to try and defeat the Enemy in 5 moves.")
  return mageBattle2 ()
  
def mageRetreat1 ():
  print ("Mage retreated from Battle 1 like a chicken! Maybe they'll win Battle 2!")
  return mageBattle2 ()
  
def wantQuit ():
  inp = input ("> ")
  if inp == "yes":
    print ("Goodbye!")
    sys.exit ()
  elif inp == "no":
    print ("Taking you to the main menu...")
    startUp ()
  else:
    print ("Ughhh...\nPLEASE type an actual answer. Just 'yes' or 'no'. It's a simple question with a simple response. Please?")
    return wantQuit ()
  
###########################################################
##################### MAGE BATTLE 2 #######################
###########################################################

def mageBattle2 ():
  print ("--------------------\n----- BATTLE 2! ----\n--------------------")
  print ("Welcome to your second Battle! Your enemy in this Battle is a Werewolf.\nYou already know how to play, so let's get started! Good luck!")
  global heroHealth, enemyHealth
  heroHealth, enemyHealth = 15, 15
  return mageLoop2 ()
  
def mageLoop2 ():
  count = 1
  for count in range(7):
    print ("--------------------\n--------------------\nYour turn!")
    print ("What do you want to do?\n- Attack\n- Block\n- Retreat")
    mageMoveChoice2 ()
    if enemyHealth <= 0:
      return mageBattle2Win ()
    mageEnemyAttack2 ()
    if heroHealth <= 0:
      return mageBattle2Lose ()
    count += 1
    if count == 6:
      return mageBattle2Tired ()
    else:
      continue
      
def mageMoveChoice2 ():
  moveChoiceInp = input ("> ")
  if moveChoiceInp == "Attack":
    return mageAttackChoice2 ()
  elif moveChoiceInp == "Block":
    return mageBlock2 ()
  elif moveChoiceInp == "Retreat":
    return mageRetreat2 ()
  else:
    print ("You can Attack, Block and Retreat. Choose one of these options.")
    return mageMoveChoice2 ()
    
def mageAttackChoice2 ():
  print ("1. Fireball\n2. Water Jet\n3. Earthquake\n4. Thorny Whip")
  print ("What attack do you want to use? Type 'Back' if you want to do something else.")
  attackChoiceInp = input ("> ")
  if attackChoiceInp == "Fireball":
    return mageFireball2 ()
  elif attackChoiceInp == "Water Jet":
    return mageWaterJet2 ()
  elif attackChoiceInp == "Earthquake":
    return mageEarthquake2 ()
  elif attackChoiceInp == "Thorny Whip":
    return mageThornyWhip2 ()
  elif attackChoiceInp == "Back":
    print ("Going back...")
    return mageMoveChoice2
  else:
    print ("That's an invalid choice. All inputs are case-sensitive. Please try again.")
    return mageAttackChoice2 ()

def mageFireball2 ():
  global enemyHealth
  attackHit = random.randint (1,5)
  if attackHit <= 3:
    print ("Werewolf has",enemyHealth,"Health!\nMage throws Fireball!\nWerewolf takes 6 DMG!\nWerewolf has",enemyHealth - 6,"Health!")
    enemyHealth -= 6
  else:
    print ("Werewolf has",enemyHealth,"Health!\nMage throws Fireball!\nFireball misses!\nWerewolf still has",enemyHealth,"Health!")

def mageWaterJet2 ():
  global enemyHealth
  attackHit = random.randint(1,7)
  if attackHit <= 4:
    print ("Werewolf has",enemyHealth,"Health!\nMage uses Water Jet!\nWerewolf takes 4 DMG!\nWerewolf has",enemyHealth - 4,"Health.")
    enemyHealth -= 4 
  else:
    print ("Werewolf has",enemyHealth,"Health!\nMage uses Water Jet!\nWater Jet misses!\nWerewolf still has",enemyHealth,"Health!")

def mageEarthquake2 ():
  global enemyHealth
  attackHit = random.randint (1,8)
  if attackHit <= 3:
    print ("Werewolf has",enemyHealth,"Health!\nMage creates an Earthquake!\nWerewolf takes 9 DMG!\nWerewolf has",enemyHealth - 9,"Health.")
  else:
    print ("Werewolf has",enemyHealth,"Health!\nMage creates an Earthquake!\nEarthquake misses!\nWerewolf still has",enemyHealth,"Health!")

def mageThornyWhip2 ():
  global enemyHealth
  attackHit = random.randint(1,4)
  if attackHit <= 3:
    print ("Werewolf has",enemyHealth,"Health!\nMage uses Thorny Whip!\nWerewolf takes 4 DMG!\nWerewolf has",enemyHealth - 4,"Health.")
    enemyHealth -= 4 
  else:
    print ("Werewolf has",enemyHealth,"Health!\nMage uses Thorny Whip!\nThorny Whip misses!\nWerewolf still has",enemyHealth,"Health!")

def mageEnemyAttack2 ():
  global heroHealth
  attackHit = random.randint (1,25)
  print ("--------------------\n---------------------\nEnemy's turn!")
  if attackHit <= 4:
    print ("Mage has",heroHealth,"Health!\nWerewolf Scratches Mage!\nScratch misses!\nMage still has",heroHealth,"Health!")
  elif attackHit > 4 <= 13:
    print ("Mage has",heroHealth,"Health!\nMage gets Bitten!\nBite deals 5 DMG!\nMage has",heroHealth - 5,"Health.")
    heroHealth -= 5
  elif attackHit > 13 <= 25:
    print ("Mage has",heroHealth,"Health!\nMage gets hit by Full Moon Rage!\nMage takes 7 DMG!\nMage has",heroHealth - 7,"Health.")
    heroHealth -= 7
  else:
    print ("error in code :/")

def mageBlock2 ():
  print ("Mage uses Block! Mage blocks Enemy's next attack!")
  print ("It's Mage's turn again!")
  return mageMoveChoice2 ()

def mageBattle2Win ():
  print ("Well done, Mage! You won your second battle! Your next Battle is the Boss Battle! It'll be hard, so you'll get 8 moves this time! Good luck!")
  return mageBattle3 ()

def mageBattle2Lose ():
  print ("Oh no, Mage! You lost! Don't worry, you'll win the next Battle!\nYour next Battle is the Boss Battle! It'll be hard, so you'll get 8 moves this time! Good luck!")
  return mageBattle3 ()

def mageBattle2Tired ():
  print ("Mage got tired of fighting! Mage lost!\nDon't worry you'll win the next Battle.\nYour next Battle is the Boss Battle! It'll be hard, so you'll get 8 moves this time! Good luck!")
  return mageBattle3 ()

def mageRetreat2 ():
  print ("Mage retreated from Battle 2!")
  mageBattle2Lose ()

############################################################
###################### MAGE BATTLE 3 #######################
############################################################

def mageBattle3 ():
  print ("--------------------\n--- BOSS BATTLE! ---\n--------------------")
  print ("Welcome to the Boss Battle! The Boss is the Hydra, a 9-headed snake!\nGood luck, you'll need it! ")
  global heroHealth, enemyHealth
  heroHealth, enemyHealth = 15, 30
  return mageLoop3 ()
  
def mageLoop3 ():
  count = 1
  for count in range(10):
    print ("--------------------\n--------------------\nYour turn!")
    print ("What do you want to do?\n- Attack\n- Block\n- Retreat")
    mageMoveChoice3 ()
    if enemyHealth <= 0:
      return mageBattle3Win ()
    mageEnemyAttack3 ()
    if heroHealth <= 0:
      return mageBattle3Lose ()
    count += 1
    if count == 9:
      return mageBattle3Tired ()
    else:
      continue

def mageMoveChoice3 ():
  moveChoiceInp = input ("> ")
  if moveChoiceInp == "Attack":
    return mageAttackChoice3 ()
  elif moveChoiceInp == "Block":
    return mageBlock3 ()
  elif moveChoiceInp == "Retreat":
    return mageRetreat3 ()
  else:
    print ("You can Attack, Block and Retreat. Choose one of these options.")
    return mageMoveChoice3 ()

def mageAttackChoice3 ():
  print ("1. Fireball\n2. Water Jet\n3. Earthquake\n4. Thorny Whip")
  print ("What attack do you want to use? Type 'Back' if you want to do something else.")
  attackChoiceInp = input ("> ")
  if attackChoiceInp == "Fireball":
    return mageFireball3 ()
  elif attackChoiceInp == "Water Jet":
    return mageWaterJet3 ()
  elif attackChoiceInp == "Earthquake":
    return mageEarthquake3 ()
  elif attackChoiceInp == "Thorny Whip":
    return mageThornyWhip3 ()
  elif attackChoiceInp == "Back":
    print ("Going back...")
    return mageMoveChoice3
  else:
    print ("That's an invalid choice. All inputs are case-sensitive. Please try again.")
    return mageAttackChoice3 ()

def mageFireball3 ():
  global enemyHealth
  attackHit = random.randint (1,5)
  if attackHit <= 3:
    print ("Hydra has",enemyHealth,"Health!\nMage throws Fireball!\nHydra takes 6 DMG!\nHydra has",enemyHealth - 6,"Health!")
    enemyHealth -= 6
  else:
    print ("Hydra has",enemyHealth,"Health!\nMage throws Fireball!\nFireball misses!\nHydra still has",enemyHealth,"Health!")

def mageWaterJet3 ():
  global enemyHealth
  attackHit = random.randint(1,7)
  if attackHit <= 4:
    print ("Hydra has",enemyHealth,"Health!\nMage uses Water Jet!\nHydra takes 4 DMG!\nHydra has",enemyHealth - 4,"Health.")
    enemyHealth -= 4 
  else:
    print ("Hydra has",enemyHealth,"Health!\nMage uses Water Jet!\nWater Jet misses!\nHydra still has",enemyHealth,"Health!")

def mageEarthquake3 ():
  global enemyHealth
  attackHit = random.randint (1,8)
  if attackHit <= 3:
    print ("Hydra has",enemyHealth,"Health!\nMage creates an Earthquake!\nHydra takes 9 DMG!\nHydra has",enemyHealth - 9,"Health.")
  else:
    print ("Hydra has",enemyHealth,"Health!\nMage creates an Earthquake!\nEarthquake misses!\nHydra still has",enemyHealth,"Health!")

def mageThornyWhip3 ():
  global enemyHealth
  attackHit = random.randint(1,4)
  if attackHit <= 3:
    print ("Hydra has",enemyHealth,"Health!\nMage uses Thorny Whip!\nHydra takes 4 DMG!\nHydra has",enemyHealth - 4,"Health.")
    enemyHealth -= 4 
  else:
    print ("Hydra has",enemyHealth,"Health!\nMage uses Thorny Whip!\nThorny Whip misses!\nHydra still has",enemyHealth,"Health!")

def mageEnemyAttack3 ():
  global heroHealth
  attackHit = random.randint (1,25)
  print ("--------------------\n--------------------\nEnemy's turn!")
  if attackHit <= 2:
    print ("Mage has",heroHealth,"Health!\nHydra Strangles Mage!\nStrangle misses!\nMage still has",heroHealth,"Health!")
  elif attackHit > 2 <= 15:
    print ("Mage has",heroHealth,"Health!\nMage gets Headbutted!\nHeadbutt deals 6 DMG! Mage has",heroHealth - 6,"Health.")
    heroHealth -= 6
  elif attackHit > 15 <= 25:
    print ("Mage has",heroHealth,"Health! Mage gets hit by Poison Fangs!\nMage takes 9 DMG!\nMage has",heroHealth - 9,"Health.")
    heroHealth -= 9
  else:
    print ("error in code :/")

def mageBlock3 ():
  print ("Mage uses Block! Mage blocks Enemy's next attacl!")
  print ("It's Mage's turn again!")
  return mageMoveChoice3 ()

def mageBattle3Win ():
  print ("Well done, Mage! You won the Boss Battle! Do you want to play again?")
  return playAgain ()

def mageBattle3Lose ():
  print ("Oh no, Mage! You lost! Do you want to play again?")
  return playAgain ()

def mageBattle3Tired ():
  print ("Mage got tired of fighting! Mage lost!\nDo you want to play again?")
  return playAgain

def mageRetreat3 ():
  print ("Mage retreated from the Boss Battle!")
  return mageBattle3Lose ()

############################################################  
####################### ASSASSIN GAME ######################
############################################################

def assassinGame ():
  print ("You are an Assassin!")
  print ("Get ready for your first battle! I'll walk you through it.")
  print ("Your first enemy is a Spy. An easy first enemy.")
  print ("In a battle, you have three options:\n1. Attack\n2. Block\n3. Retreat")
  print ("1When you attack, you can use the four moves mentioned earlier.\nBlocking will block the next attack the enemy makes, but you only have a limited number of moves to defeat the enemy, so don't overuse it.\nOnly retreat when necessary. You won't die, but you won't win the battle either.")
  print ("Now it's time for your first move!")  
  global heroHealth, enemyHealth
  heroHealth, enemyHealth = 30, 25
  return assassinLoop1 ()
  
############################################################
#################### ASSASSIN BATTLE 1 #####################
############################################################

def assassinLoop1 ():
  count = 1
  for count in range(7):
    print ("--------------------\n--------------------\nYour turn!")
    print ("What do you want to do?\n- Attack\n- Block\n- Retreat")
    assassinMoveChoice1 ()
    if enemyHealth <= 0:
      return assassinBattle1Win ()
    assassinEnemyAttack1 ()
    if heroHealth <= 0:
      return assassinBattle1Lose ()
    count += 1
    if count == 6:
      return assassinBattle1Tired ()
    else:
      continue
      
def assassinMoveChoice1 ():
  moveChoiceInp = input ("> ")
  if moveChoiceInp == "Attack":
    return assassinAttackChoice1 ()
  elif moveChoiceInp == "Block":
    return assassinBlock1 ()
  elif moveChoiceInp == "Retreat":
    return assassinRetreat1 ()
  else:
    print ("You can Attack, Block and Retreat. Choose one of these options.")
    return assassinMoveChoice1 ()
    
def assassinAttackChoice1 ():
  print ("1. Knife Plunge\n2. Bullets\n3. Hand-to-hand\n4. Precise Snipe")
  print ("What attack do you want to use? Type 'Back' if you want to do something else.")
  attackChoiceInp = input ("> ")
  if attackChoiceInp == "Knife Plunge":
    return assassinKnife1 ()
  elif attackChoiceInp == "Bullets":
    return assassinBullets1 ()
  elif attackChoiceInp == "Hand-to-hand":
    return assassinFight1 ()
  elif attackChoiceInp == "Precise Snipe":
    return assassinSnipe1 ()
  elif attackChoiceInp == "Back":
    print ("Going back...")
    return assassinMoveChoice1 ()
  else:
    print ("That's an invalid choice. All inputs are case-sensitive. Please try again.")
    return assassinAttackChoice1 ()
    
def assassinKnife1 ():
  global enemyHealth
  attackHit = random.randint (1,10)
  if attackHit <= 7:
    print ("Spy has",enemyHealth,"Health!\nAssassin uses Knife Plunge!\nSpy takes 8 DMG!\nSpy has",enemyHealth - 8,"Health!")
    enemyHealth -= 8
  else:
    print ("Spy has",enemyHealth,"Health!\nAssassin uses Knife Plunge!\nKnife Plunge misses!\nSpy still has",enemyHealth,"Health!")

def assassinBullets1 ():
  global enemyHealth
  attackHit = random.randint (1,10)
  if attackHit <= 6:
    print ("Spy has",enemyHealth,"Health!\nAssassin uses Bullets!\nSpy takes 12 DMG!\nSpy has",enemyHealth - 12,"Health!")
    enemyHealth -= 12
  else:
    print ("Spy has",enemyHealth,"Health!\nAssassin uses Bullets!\nBullets misses!\nSpy still has",enemyHealth,"Health!")    

def assassinFight1 ():
  global enemyHealth
  attackHit = random.randint (1,4)
  if attackHit <= 3:
    print ("Spy has",enemyHealth,"Health!\nAssassin uses Hand-to-hand!\nSpy takes 9 DMG!\nSpy has",enemyHealth - 9,"Health!")
    enemyHealth -= 9
  else:
    print ("Spy has",enemyHealth,"Health!\nAssassin uses Hand-to-hand!\nHand-to-hand misses!\nSpy still has",enemyHealth,"Health!") 

def assassinSnipe1 ():
  global enemyHealth
  attackHit = random.randint (1,10)
  if attackHit <= 8:
    print ("Spy has",enemyHealth,"Health!\nAssassin uses Precise Snipe!\nSpy takes 15 DMG!\nSpy has",enemyHealth - 15,"Health!")
    enemyHealth -= 15
  else:
    print ("Spy has",enemyHealth,"Health!\nAssassin uses Precise Snipe!\nPrecise Snipe misses!\nSpy still has",enemyHealth,"Health!")
    
def assassinEnemyAttack1 ()
  global heroHealth
  attackHit = random.randint (1,25)
  print ("--------------------\n--------------------\nEnemy's turn!")
  if attackHit <= 5:
    print ("Assassin has",heroHealth,"Health!\nSpy uses Dagger Throw!\nDagger Throw misses!\nMage still has",heroHealth,"Health!")
  elif attackHit > 5 <= 18:
    print ("Assassin has",heroHealth,"Health!\nAssassin gets Ambushed!\nAmbush deals 6 DMG!\nAssassin has",heroHealth - 6,"Health!")
    heroHealth -= 6
  elif attackHit > 18 <= 25:
    print ("Assassin has",heroHealth,"Health!\nAssassin gets shot by Pistol!\nPistol deals 8 DMG!\nAssassin has",enemyHealth - 8"Health!")
    heroHealth -= 8
  else:
    print ("error in code :/")
    
def assassinBlock1 ():
  print ("Assassin uses Block! Assassin blocks Enemy's next attack!")
  print ("It's Assassin's turn again!")
  return assassinMoveChoice1 ()

def assassinBattle1Win ():
  print ("Well done, Assassin! You won your first Battle! Get ready, you're about to start Battle 2!")
  return assassinBattle2 ()  
  
def assassinBattle1Lose ():
  print ("Oh no, Assassin! You lost! Don't worry, you'll win the next Battle!")
  return assassinBattle2 ()
  
def assassinBattle1Tired ():
  print ("Assassin got tired of fighting! Assassin lost!\nDon't worry you'll win the next Battle. Just remember to try and defeat the Enemy in 5 moves.")
  return assassinBattle2 ()

def assassinRetreat1 ():
  print ("Assassin retreated from Battle 1 like a chicken! Maybe they'll win Battle 2!")
  return assassinBattle2 ()
  
############################################################
#################### ASSASSIN BATTLE 2 #####################
############################################################

def asLoop2 ():
  count = 1
  for count in range(7):
    print ("--------------------\n--------------------\nYour turn!")
    print ("What do you want to do?\n- Attack\n- Block\n- Retreat")
    asMoveChoice2 ()
    if enemyHealth <= 0:
      return asBattle2Win ()
    asEnemyAttack2 ()
    if heroHealth <= 0:
      return asBattle2Lose ()
    count += 1
    if count == 6:
      return asBattle2Tired ()
    else:
      continue  
      
def asMoveChoice2 ():
  moveChoiceInp = input ("> ")
  if moveChoiceInp == "Attack":
    return asAttackChoice2 ()
  elif moveChoiceInp == "Block":
    return asBlock2 ()
  elif moveChoiceInp == "Retreat":
    return asRetreat2 ()
  else:
    print ("You can Attack, Block and Retreat. Choose one of these options.")
    return asMoveChoice2 ()  

def asAttackChoice2 ():
  
############################################################
########################## EXTRAS ##########################
############################################################

def playAgain ():
  inp = input ("> ")
  if inp == "yes":
    print ("Restarting...")
    return startUp ()
  elif inp == "no":
    print ("Do you want to quit?")
    return wantQuit
  else:
    print ("Please type 'yes' or 'no'.")
    return playAgain ()


startUp ()
  
  
  


