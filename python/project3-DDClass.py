#Define character classes and introduce topic of quiz.
Fighter = 0
Rogue = 0
Wizard = 0
Cleric = 0
Bard = 0

print("\n \n This is a short quiz to determine which class you might enjoy playing in Dungeons and Dragons.\n")

#Begin questionnaire - easy to add more questions or expand if character classes are added in the future.

q1_answer = input("Which attribute do you want your character to maximize? \na) Stength \nb) Dexterity \nc) Intelligence \nd) Wisdom \ne) Charisma\n")

if q1_answer == "a":
  Fighter += 1
elif q1_answer == "b":
  Rogue += 1
elif q1_answer == "c":
  Wizard +=1
elif q1_answer == "d":
  Cleric +=1
elif q1_answer == "e":
  Bard +=1
else:
  print("Sorry, I didn't understand your response. I can only interpret 'a-e'.")
  
q2_answer = input("How would your character handle an enraged ogre? \na) Charge into the fray! \nb) Try to find a sneakier solution. Or at least attack without being seen first. \nc) Fireball! \nd) Lots of faith and lots of plate-mail. \ne) Play 'All Star' by Smash Mouth and encourage the party. \n")

if q2_answer == "a":
  Fighter += 1
elif q2_answer == "b":
  Rogue += 1
elif q2_answer == "c":
  Wizard +=1
elif q2_answer == "d":
  Cleric +=1
elif q2_answer == "e":
  Bard +=1
else:
  print("Sorry, I didn't understand your response. I can only interpret 'a-e'.")
  
q3_answer = input("What is the best way to stop a tavern brawl? \na) Knock everyone else down! \nb) Why stop it? No one pays attention to coinpurses during a fight. \nc) Fireball! \nd) Remind the patrons of the divine, and if that fails, be prepared to offer healing afterwards. \ne) You aren't sure - the brawl started because you were playing All Star by Smash Mouth.\n")

if q3_answer == "a":
  Fighter += 1
elif q3_answer == "b":
  Rogue += 1
elif q3_answer == "c":
  Wizard +=1
elif q3_answer == "d":
  Cleric +=1
elif q3_answer == "e":
  Bard +=1
else:
  print("Sorry, I didn't understand your response. I can only interpret 'a-e'.")

q4_answer = input("What motivates you for adventure? \na) Crush your enemies. See them driven before you. \nb) Money. Or valuable jewels. Or valuable magical items. Really anything that can be fenced. \nc) Fireball! \nd) You take pride knowing if you weren't there to heal the party they'd never survive their shenanigans. \ne) You want to fill the Realms with the sweet sounds of the Shrek soundtrack.\n")

if q4_answer == "a":
  Fighter += 1
elif q4_answer == "b":
  Rogue += 1
elif q4_answer == "c":
  Wizard +=1
elif q4_answer == "d":
  Cleric +=1
elif q4_answer == "e":
  Bard +=1
else:
  print("Sorry, I didn't understand your response. I can only interpret 'a-e'.")
  
  
  #Determine results of questionaire and print results. Also contains array to list back choices made in the event of a split vote/tie.
  
if Fighter > Rogue and Fighter > Wizard and Fighter > Cleric and Fighter > Bard:
  print("Once more unto the breach! You might enjoy playing a FIGHTER.")
elif Rogue > Fighter and Rogue > Wizard and Rogue > Cleric and Rogue > Bard:
  print("You're the most 'grounded' party member. Glory? Magic trinkets? Someone's gotta pay the BILLS. You might enjoy playing a ROGUE.")
elif Wizard > Fighter and Wizard > Rogue and Wizard > Cleric and Wizard > Bard:
   print("FIREBALL!!!!!! I mean, uh...you might enjoy playing a WIZARD.")
elif Cleric > Fighter and Cleric > Rogue and Cleric > Wizard and Cleric > Bard:
  print("The pious life is rough in D&D, always needing to heal everyone. But here's a benefit - you can also wear platemail and carry a warhammer. You might enjoy playing a CLERIC.")
elif Bard > Fighter and Bard > Rogue and Bard > Wizard and Bard > Cleric:
  print("You are here to party. Which is strange, because it's a role-playing game. You are role-playing someone partying in fantasy. Oh well, your antics are fun and party buffs are great. You might enjoy playing a BARD.")
else:
  print("Too difficult to decide... Maybe you just need to multi-class! You could be a mix of...")
  PChars = []
  if Fighter > 0:
    PChars.append("Fighter")
  if Rogue > 0:
    PChars.append("Rogue")
  if Wizard > 0:
    PChars.append("Wizard")
  if Cleric > 0:
    PChars.append("Cleric")
  if Bard > 0:
    PChars.append("Bard")
  for PChar in PChars:
    print(PChar)